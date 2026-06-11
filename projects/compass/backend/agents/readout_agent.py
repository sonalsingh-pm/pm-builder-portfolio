"""
Readout Agent — turns a finished discovery brief into an executive-ready deck.

Same pattern as every other agent: a job description, an input, and a strict
output contract. The only difference is that this agent's output contract is
slides instead of brief sections.

Design rule: slide 1 (the executive summary) must stand completely alone.
If the executive stops reading after slide 1, they still know the problem,
the size of the opportunity, the competition, the biggest risk, and the ask.
"""

from .gemini_client import call_gemini_json

SYSTEM = """You are an executive communications specialist who turns product discovery research into concept decks for senior leadership.

Your reader is a VP or C-level executive with 3 minutes. They did not read the research. They will not read it. Your deck is everything they will ever see.

LANGUAGE RULES — follow these exactly:
- Plain English. No jargon. No buzzwords.
- Forbidden words: leverage, synergy, ecosystem, PMF, friction, pivot, moat, whitespace, north star, unlock, scalable, robust, seamless, delight, empower.
- Short sentences. Every word must earn its place on the slide.
- Numbers over adjectives. "Owners lose 15-25% of inventory monthly" beats "significant waste".
- Each slide must make sense on its own — never reference another slide.
- Define any concept the first time it appears. Never assume the reader knows a term from the research.

SLIDE DISCIPLINE:
- Headlines are full sentences that carry the message. "Competitors all require daily manual counts" — not "Competitive Landscape".
- Bullets are 15 to 25 words. Short, but dense: every bullet should earn a nod, not a shrug.
- Use a concrete number in every bullet where the research provides one. "Owners lose 15-25% of inventory monthly" beats "owners lose significant inventory".
- No bullet may restate another bullet.
- A slide with thin content is a failure. Pull the strongest specifics from the research: named competitors, dollar figures, percentages, named segments.

Always output valid JSON only — no markdown, no explanation outside the JSON."""


def run(brief: dict, synthesis: dict, eval_scores: dict) -> dict:
    framing     = brief.get("problem_framing", {})
    market      = brief.get("market_research", {})
    competitive = brief.get("competitive_analysis", {})
    sizing      = brief.get("opportunity_sizing", {})
    risk        = brief.get("risk_assessment", {})

    competitors = competitive.get("competitors", [])
    risks       = risk.get("risks", [])

    prompt = f"""
Turn this completed product discovery research into a 6-slide executive concept deck.

RESEARCH FINDINGS:

PROBLEM (framing):
- Primary user: {framing.get("primary_user", "")}
- Reframed problem: {framing.get("reframed_problem", "")}
- Current struggle: {framing.get("current_struggle", "")}
- Job to be done: {framing.get("jtbd_statement", "")}

MARKET:
- Definition: {market.get("market_definition", "")}
- TAM: {sizing.get("tam", {}).get("value", "")} — {sizing.get("tam", {}).get("calculation", "")}
- SAM: {sizing.get("sam", {}).get("value", "")} — {sizing.get("sam", {}).get("rationale", "")}
- SOM: {sizing.get("som", {}).get("value", "")} — {sizing.get("som", {}).get("rationale", "")}
- Growth: {market.get("growth_rate", "")} — {market.get("growth_driver", "")}
- Beachhead segment: {sizing.get("beachhead_segment", "")}

COMPETITION:
{chr(10).join(f"- {c.get('name','')}: strength = {c.get('primary_strength','')}; gap = {c.get('critical_gap','')}" for c in competitors)}
- Pattern: {competitive.get("competitive_pattern", "")}
- Differentiation: {competitive.get("differentiation_opportunity", "")}

RISKS:
{chr(10).join(f"- {r.get('title','')} (likelihood {r.get('likelihood','')}, impact {r.get('impact','')}): {r.get('description','')} Mitigation: {r.get('mitigation','')}" for r in risks)}
- Biggest open question: {risk.get("biggest_open_question", "")}
- Pre-mortem: {risk.get("pre_mortem_scenario", "")}

VERDICT (from synthesis):
- Recommendation: {synthesis.get("recommendation", "")}
- Rationale: {synthesis.get("recommendation_rationale", "")}
- Conditions before proceeding: {synthesis.get("proceed_conditions", [])}
- Next steps: {synthesis.get("next_steps", [])}
- Research quality score: {eval_scores.get("overall_score", "")}/100

Return a JSON object with exactly this structure:

{{
  "deck_title": "A short, concrete name for this opportunity (4-7 words). Not a product name — a description an exec instantly understands.",
  "deck_subtitle": "One line: who it serves and what it does for them.",
  "slides": [
    {{
      "type": "exec_summary",
      "title": "Everything you need in one slide",
      "headline": "One bold sentence: the single most important takeaway of the entire research.",
      "recommendation": "{synthesis.get("recommendation", "INVESTIGATE")}",
      "summary_points": [
        {{"label": "Problem", "text": "15-25 words with the cost to the user, quantified"}},
        {{"label": "Market", "text": "15-25 words with TAM, growth rate, and the beachhead segment"}},
        {{"label": "Competition", "text": "15-25 words naming the dominant pattern and the specific opening it creates"}},
        {{"label": "Biggest risk", "text": "15-25 words: the risk that decides everything and how we test it"}}
      ],
      "the_ask": "One sentence: exactly what you want from this executive (a decision, budget, or time-boxed validation)."
    }},
    {{
      "type": "problem",
      "title": "Full-sentence headline carrying the problem message",
      "narrative": "3-4 short sentences making the exec FEEL the problem. Open with the human reality, then ground it with the strongest specifics from the research.",
      "who_hurts": "One full sentence naming the user precisely, with context on their situation",
      "cost_of_inaction": "One full sentence: what it costs them today, quantified wherever the research allows"
    }},
    {{
      "type": "market",
      "title": "Full-sentence headline carrying the market message",
      "stats": [
        {{"label": "TAM", "value": "$X", "note": "what this number means in plain words"}},
        {{"label": "SAM", "value": "$X", "note": "..."}},
        {{"label": "SOM (3yr)", "value": "$X", "note": "..."}}
      ],
      "narrative": "2-3 sentences covering the growth rate, what is driving it, and why the beachhead segment adopts first. Include numbers. Label estimates as estimates."
    }},
    {{
      "type": "competition",
      "title": "Full-sentence headline carrying the competitive insight",
      "competitors": [
        {{"name": "Product name", "strength": "10-16 words, specific", "gap": "10-16 words: the specific thing it cannot do that this problem requires"}}
      ],
      "takeaway": "One sentence: the specific opening this creates for us."
    }},
    {{
      "type": "risks",
      "title": "Full-sentence headline that is honest about the biggest threat",
      "risks": [
        {{"title": "Risk name", "severity": "high/medium/low", "one_liner": "the risk and how it materializes, 15-22 words", "mitigation": "the de-risking action, 10-16 words, concrete enough to execute"}}
      ],
      "kill_condition": "One sentence: the specific finding that would mean we should stop."
    }},
    {{
      "type": "recommendation",
      "title": "Full-sentence headline stating the call",
      "recommendation": "{synthesis.get("recommendation", "INVESTIGATE")}",
      "rationale": "2-3 sentences: why this call, naming the specific findings that drove it.",
      "conditions": ["Each condition in one line, max 18 words"],
      "next_steps": ["Step with owner and timeframe, one line each, max 3 steps"]
    }}
  ]
}}

Include the 3 most decision-relevant risks only. Include up to 4 competitors.
"""
    return call_gemini_json(prompt, SYSTEM)
