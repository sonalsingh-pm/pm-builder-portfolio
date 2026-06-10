from .gemini_client import call_gemini_json

SYSTEM = """You are a product risk analyst who writes pre-mortem analyses for senior PMs.
Identify risks that are specific to this problem and market — not generic startup risks.
For each risk, explain the mechanism: how exactly does this risk materialize?
If the input contains VERIFIED USER CLARIFICATIONS, those facts are confirmed. Your risks must be specific to the confirmed user and use case — do not write risks for a generic or different version of this problem.
Always output valid JSON only — no markdown, no explanation outside the JSON."""

def run(problem_statement: str, competitive_pattern: str, beachhead_segment: str) -> dict:
    prompt = f"""
Identify the top product and market risks for building a product that addresses this problem:

PROBLEM: {problem_statement}
COMPETITIVE PATTERN: {competitive_pattern}
TARGET SEGMENT: {beachhead_segment}

Return a JSON object with exactly these fields:

{{
  "risks": [
    {{
      "category": "One of: market, technical, competitive, regulatory, adoption, business_model",
      "title": "Short risk name (5-8 words)",
      "description": "What the risk is and why it exists in this specific context.",
      "mechanism": "Exactly how this risk would materialize. What is the failure sequence?",
      "likelihood": "high, medium, or low",
      "impact": "high, medium, or low",
      "mitigation": "One specific action that reduces this risk before product launch."
    }}
  ],
  "biggest_open_question": "The single most important unknown that should be answered before committing to this opportunity.",
  "pre_mortem_scenario": "Imagine it is 18 months from now and the product has failed. What is the most likely cause?"
}}

Include exactly 5 risks. Prioritize risks specific to this problem over generic risks.
"""
    return call_gemini_json(prompt, SYSTEM)
