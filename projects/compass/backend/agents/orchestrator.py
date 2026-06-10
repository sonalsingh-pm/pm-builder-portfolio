import asyncio
from concurrent.futures import ThreadPoolExecutor
from . import (
    internal_search_agent,
    problem_framing_agent,
    market_research_agent,
    competitive_analysis_agent,
    opportunity_sizing_agent,
    risk_assessment_agent,
    eval_agent,
    improve_agent,
    synthesis_agent,
)

executor = ThreadPoolExecutor(max_workers=8)

async def run_in_thread(fn, *args):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(executor, fn, *args)

async def safe_run(fn, *args):
    """
    Safety wrapper around every agent call (graceful degradation).

    - If the agent returns unreadable JSON, retry once before giving up.
    - If the agent crashes, return a {"_failed": True} marker instead of
      raising — so one failed agent never destroys the other agents' work.
    """
    try:
        result = await run_in_thread(fn, *args)
        if isinstance(result, dict) and result.get("parse_error"):
            result = await run_in_thread(fn, *args)  # one retry
        if isinstance(result, dict) and result.get("parse_error"):
            return {"_failed": True, "error": "The AI returned an unreadable response twice."}
        return result
    except Exception as e:
        return {"_failed": True, "error": str(e)[:200]}

SECTION_KEYS = ["problem_framing", "market_research", "competitive_analysis", "opportunity_sizing", "risk_assessment"]

async def run(problem_statement: str) -> dict:

    # ── Phase 1: Internal Search ──────────────────────────────────────────────
    internal = await run_in_thread(internal_search_agent.run, problem_statement)

    if internal["status"] == "active_project":
        return {
            "phase": "stopped_active_project",
            "internal": internal,
            "message": internal["message"],
        }

    # ── Phase 2a: Problem Framing first (others depend on it) ────────────────
    framing = await safe_run(problem_framing_agent.run, problem_statement)

    # If framing failed, downstream agents fall back to the raw problem
    # statement instead of receiving empty context.
    reframed     = framing.get("reframed_problem", problem_statement)
    primary_user = framing.get("primary_user", "")
    jtbd         = framing.get("jtbd_statement", problem_statement)

    # ── Phase 2b: Market + Competitive in parallel ────────────────────────────
    market, competitive = await asyncio.gather(
        safe_run(market_research_agent.run, problem_statement, reframed),
        safe_run(competitive_analysis_agent.run, problem_statement, jtbd),
    )

    # ── Phase 2c: Sizing + Risk in parallel ───────────────────────────────────
    sizing, risk = await asyncio.gather(
        safe_run(opportunity_sizing_agent.run, problem_statement, market.get("tam_estimate", ""), primary_user),
        safe_run(risk_assessment_agent.run, problem_statement, competitive.get("competitive_pattern", ""), primary_user),
    )

    brief = {
        "problem_framing":      framing,
        "market_research":      market,
        "competitive_analysis": competitive,
        "opportunity_sizing":   sizing,
        "risk_assessment":      risk,
    }

    # Sections that completed vs. sections that failed
    ok_keys = [k for k in SECTION_KEYS if not brief[k].get("_failed")]

    # If every section failed, the AI service is down — return one honest error.
    if not ok_keys:
        return {
            "phase": "error",
            "internal": internal,
            "message": "The AI service could not complete any research right now. Please wait a minute and try again.",
        }

    # ── Phase 3: Eval — completed sections scored IN PARALLEL ─────────────────
    # Failed sections are not graded: averaging in a zero would unfairly
    # punish the sections that did complete.
    section_eval_results = await asyncio.gather(*[
        safe_run(eval_agent.score_section, key, brief[key])
        for key in ok_keys
    ])

    section_scores = {key: result for key, result in zip(ok_keys, section_eval_results)}
    raw_scores = [v.get("section_score", 0) for v in section_scores.values() if not v.get("_failed")]
    overall = round(sum(raw_scores) / len(raw_scores)) if raw_scores else 0

    scores = {
        "section_scores": section_scores,
        "overall_score": overall,
        "confidence_label": (
            "High confidence — ready to share with stakeholders" if overall >= 75
            else "Medium confidence — review weak sections before presenting" if overall >= 50
            else "Low confidence — significant gaps need to be addressed"
        ),
        "sections_refined": [],
    }

    # ── Phase 4: Auto-refine — only the single lowest section ────────────────
    # Capped at 1 section to keep total time under 2 minutes.
    # Only completed sections with a real score are eligible.
    scored_keys = [k for k in ok_keys if not section_scores.get(k, {}).get("_failed")]

    if scored_keys:
        lowest_key = min(scored_keys, key=lambda k: section_scores.get(k, {}).get("section_score", 100))
        lowest_score = section_scores.get(lowest_key, {}).get("section_score", 100)

        if lowest_score < 75:
            original_eval  = section_scores[lowest_key]
            original_score = original_eval.get("section_score", 0)

            improved = await safe_run(improve_agent.run, lowest_key, brief[lowest_key], original_eval, problem_statement)

            # Only accept the rewrite if it actually succeeded
            if not improved.get("_failed"):
                new_eval  = await safe_run(eval_agent.score_section, lowest_key, improved)
                if not new_eval.get("_failed"):
                    new_score = new_eval.get("section_score", original_score)
                    new_eval["iterations"] = [original_score, new_score]

                    brief[lowest_key]                    = improved
                    scores["section_scores"][lowest_key] = new_eval
                    scores["sections_refined"]           = [lowest_key]

                    # Recalculate overall
                    updated_scores = [v.get("section_score", 0) for v in scores["section_scores"].values() if not v.get("_failed")]
                    scores["overall_score"] = round(sum(updated_scores) / len(updated_scores))

    # ── Phase 5: Synthesis ────────────────────────────────────────────────────
    synthesis = await safe_run(synthesis_agent.run, brief, scores)
    if synthesis.get("_failed"):
        synthesis = {}  # frontend simply hides the recommendation box

    return {
        "phase":     "complete",
        "internal":  internal,
        "brief":     brief,
        "eval":      scores,
        "synthesis": synthesis,
    }
