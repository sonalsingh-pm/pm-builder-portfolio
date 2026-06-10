from .gemini_client import call_gemini_json

SYSTEM = """You are a chief product officer evaluating the quality of a product discovery brief.
Score each section against specific PM quality criteria. Be honest — a mediocre brief should score 40-60, not 80.
Always output valid JSON only — no markdown, no explanation outside the JSON."""

RUBRIC = {
    "problem_framing": [
        "User is named specifically, not as a generic persona",
        "JTBD statement names a concrete situation, motivation, and outcome",
        "Current struggle is specific enough that the user would recognize themselves",
        "Reframed problem is clearer than the original input"
    ],
    "market_research": [
        "TAM estimate includes visible math with labeled assumptions",
        "Growth rate cites a specific source or methodology",
        "Trends are current and specific, not generic",
        "Market maturity assessment includes a justification"
    ],
    "competitive_analysis": [
        "Names at least 3 specific, real competitors by product name",
        "Each competitor gap is specific, not generic weakness",
        "Differentiation opportunity is concrete and defensible",
        "Competitive pattern explains why the gap exists, not just that it exists"
    ],
    "opportunity_sizing": [
        "Uses bottom-up methodology with visible math",
        "Every assumption is labeled as an assumption",
        "SAM is a logical subset of TAM with clear rationale",
        "SOM is grounded in realistic capture rate for the stage of company"
    ],
    "risk_assessment": [
        "Risks are specific to this problem, not generic startup risks",
        "Each risk includes a mechanism explaining how it materializes",
        "Pre-mortem scenario is specific and plausible",
        "At least one mitigation action is concrete enough to execute"
    ]
}

def score_section(section_key: str, section_data: dict) -> dict:
    """Score a single section independently. Used by the auto-refine loop."""
    criteria = RUBRIC.get(section_key, [])
    if not criteria:
        return {}
    prompt = f"""
Score this section of a product discovery brief against the following quality rubric.

SECTION: {section_key}
CONTENT: {section_data}

RUBRIC CRITERIA (score each 0-10):
{chr(10).join(f"- {c}" for c in criteria)}

Return a JSON object with exactly these fields:
{{
  "criteria_scores": [
    {{"criterion": "exact criterion text", "score": 0-10, "reason": "one sentence"}}
  ],
  "section_score": 0-100,
  "strongest_element": "what this section does best",
  "weakest_element": "the most important thing missing or weak",
  "suggested_action": "one specific action to improve this section"
}}
"""
    # temperature=0: graders must be consistent. The same brief should get
    # the same score every time — a noisy grader makes scores untrustworthy.
    return call_gemini_json(prompt, SYSTEM, temperature=0)


def run(brief: dict) -> dict:
    scores = {}
    for section, criteria in RUBRIC.items():
        section_data = brief.get(section, {})
        prompt = f"""
Score this section of a product discovery brief against the following quality rubric.

SECTION: {section}
CONTENT: {section_data}

RUBRIC CRITERIA (score each 0-10):
{chr(10).join(f"- {c}" for c in criteria)}

Return a JSON object with exactly these fields:
{{
  "criteria_scores": [
    {{"criterion": "exact criterion text", "score": 0-10, "reason": "one sentence explaining the score"}}
  ],
  "section_score": 0-100 (average of criteria scores scaled to 100),
  "strongest_element": "what this section does best",
  "weakest_element": "the most important thing missing or weak",
  "suggested_action": "one specific action the PM could take to improve this section"
}}
"""
        result = call_gemini_json(prompt, SYSTEM, temperature=0)
        scores[section] = result

    # Calculate overall score
    section_scores = []
    for section, result in scores.items():
        if "section_score" in result:
            section_scores.append(result["section_score"])

    overall = round(sum(section_scores) / len(section_scores)) if section_scores else 0

    return {
        "section_scores": scores,
        "overall_score": overall,
        "confidence_label": (
            "High confidence — ready to share with stakeholders" if overall >= 75
            else "Medium confidence — review weak sections before presenting" if overall >= 50
            else "Low confidence — significant gaps need to be addressed"
        )
    }
