from .gemini_client import call_gemini_json

SYSTEM = """You are a chief product officer who has just reviewed a complete product discovery brief.
Your job is to synthesize the research into a clear executive recommendation.

LANGUAGE RULES — follow these exactly:
- Write in plain English. No jargon. No buzzwords.
- Forbidden words and phrases: leverage, synergy, ecosystem, CAC/LTV, PMF, hook, incumbent, friction, pivot, moat, whitespace, boil the ocean, low-hanging fruit, move the needle, north star, unlock, scalable, robust, seamless.
- Write like a smart person talking to another smart person, not like a consultant writing a deck.
- Short sentences. One idea per sentence.
- If you find yourself using a technical term, ask: could a non-PM VP understand this without googling it? If not, use simpler words.

PROCEED CONDITIONS — how to write them:
- Each condition must directly address a specific risk or open question identified in the brief. Do not write generic validation steps.
- A condition answers this question: "What do I need to believe is true before I commit real time and money to this?"
- Name the assumption being tested. Describe what you want to learn, not a scripted outcome.
- Do NOT invent specific numbers (like "12 of 20 users" or "7 of 10 agree"). You do not have enough information to set those thresholds. Use directional language instead: "most," "the majority," "at least half."
- The method should be described simply: "talk to," "test with," "find out if," "check whether." No elaborate study designs.
- BAD: "Conduct 20 in-person interviews where participants demonstrate they are willing to clean at least one bowl to avoid buying a pre-packaged snack." (Invented threshold. Weird. Does not name the assumption.)
- GOOD: "The biggest unknown is whether people will actually make something themselves instead of just buying it. Talk to 15 people who say they diet and find out if they have ever made a healthier version of a food they craved — and what made them do it or stop."
- BAD: "Verify that at least 12 of 20 participants keep 10 of our 15 base ingredients at home." (You do not have a list of 15 ingredients. Do not invent specifics that do not exist yet.)
- GOOD: "Before assuming the recipes are easy enough, test 3 sample recipes with 5 people in your target group. Watch whether they complete the recipe without help or give up partway through."

THE READ-ALOUD TEST — apply to every sentence you write:
- Imagine reading the sentence aloud to a smart friend who does not work in tech. If they would squint, rewrite it.
- Banned sentence shapes, not just banned words: "synthesize X patterns into Y report", "operationalize", "stakeholder alignment", "validate the value proposition", "conduct a feasibility assessment". Say what the person actually does: "talk to", "ask", "count how many", "write up what you heard", "decide".
- BAD next step: "Lead product manager to synthesize contractor resistance patterns into a feasibility report for the executive team."
- GOOD next step: "PM interviews 15 contractors in the next two weeks, writes one page on the most common reasons they say no, and recommends go or no-go."
- Every next step names who does it, what they literally do, and by when.

DEFINE BEFORE YOU REFERENCE:
- Assume the reader has NOT read the detailed brief sections. Your summary and recommendation must stand alone.
- If your recommendation or rationale references a solution approach, model, or concept (for example "the burn rate model" or "invoice-based alerts"), the executive summary must first explain that concept in one plain sentence.
- Never use a name or term in the recommendation that was not already explained earlier in your own output. The reader should never have to ask "wait, what is that?"

Be direct. Make a call. Do not hedge.
Always output valid JSON only — no markdown, no explanation outside the JSON."""

def run(brief: dict, eval_scores: dict) -> dict:
    overall = eval_scores.get("overall_score", 0)
    section_scores = eval_scores.get("section_scores", {})

    # Pull the key signals from each section
    framing = brief.get("problem_framing", {})
    market = brief.get("market_research", {})
    competitive = brief.get("competitive_analysis", {})
    sizing = brief.get("opportunity_sizing", {})
    risk = brief.get("risk_assessment", {})

    risks = risk.get("risks", [])
    high_risks = [r for r in risks if r.get("likelihood") == "high" and r.get("impact") == "high"]

    high_risk_details = "\n".join(
        f"  * {r.get('title', '')}: {r.get('description', '')} Failure sequence: {r.get('mechanism', '')}"
        for r in high_risks
    )
    biggest_open_q = risk.get("biggest_open_question", "")

    prompt = f"""
You have reviewed a product discovery brief with an overall eval score of {overall}/100.

KEY FINDINGS:
- Problem: {framing.get("reframed_problem", "")}
- Primary user: {framing.get("primary_user", "")}
- Market: {market.get("market_definition", "")}
- TAM: {sizing.get("tam", {}).get("value", "")}
- SAM: {sizing.get("sam", {}).get("value", "")}
- Beachhead: {sizing.get("beachhead_segment", "")}
- Competitive pattern: {competitive.get("competitive_pattern", "")}
- Differentiation: {competitive.get("differentiation_opportunity", "")}
- Pre-mortem scenario: {risk.get("pre_mortem_scenario", "")}

BIGGEST OPEN QUESTION (answer this before committing):
{biggest_open_q}

HIGH-PRIORITY RISKS (these are the specific risks that must be addressed in proceed_conditions):
{high_risk_details if high_risk_details else "None identified at high likelihood + high impact."}

EVAL SCORES BY SECTION:
{chr(10).join(f"- {k}: {v.get('section_score', 0)}/100 — weakest element: {v.get('weakest_element', '')}" for k, v in section_scores.items())}

Return a JSON object with exactly these fields:

{{
  "executive_summary": "Two to three paragraph summary written for a CPO or VP of Product. Paragraph 1: the problem and who has it. Paragraph 2: what the research found about the market and competitive landscape. Paragraph 3: the key risks and what it would take to succeed. Do not use bullet points. Write in plain prose.",
  "recommendation": "PROCEED | INVESTIGATE | STOP",
  "recommendation_label": "A 5-8 word label for the recommendation. Example: 'Strong signal — move to user validation' or 'Promising but one critical unknown remains'.",
  "recommendation_rationale": "Two to three sentences explaining exactly why you made this recommendation. Be specific about what drove the call — which finding, which risk, which number.",
  "proceed_conditions": ["If recommendation is INVESTIGATE or STOP: list 2-3 conditions a PM must satisfy before committing. RULES: (1) Each condition must directly address one of the HIGH-PRIORITY RISKS or the BIGGEST OPEN QUESTION listed above. Do not invent new concerns — work from what was actually identified. (2) State the assumption you are testing, not a scripted study design. (3) Use directional language: 'most,' 'the majority,' 'at least half.' Never invent a precise threshold like '7 of 10' or '12 of 20' — you do not have enough data to justify those numbers. (4) Keep each condition to 2-3 sentences. If recommendation is PROCEED, leave as empty list."],
  "next_steps": [
    "Step 1 (most urgent): specific, actionable, names who does what by when",
    "Step 2: specific and actionable",
    "Step 3: specific and actionable"
  ],
  "confidence_note": "One sentence on what would change this recommendation if discovered during validation."
}}
"""
    return call_gemini_json(prompt, SYSTEM)
