from .gemini_client import call_gemini_json

SYSTEM = """You are a strategy analyst who builds bottom-up market size models.
Show your math. Label every number that is an assumption.
Do not use round numbers without explaining why. Prefer bottom-up over top-down estimates.
Always output valid JSON only — no markdown, no explanation outside the JSON."""

def run(problem_statement: str, tam_estimate: str, primary_user: str) -> dict:
    prompt = f"""
Size the opportunity for the following problem using bottom-up methodology:

PROBLEM: {problem_statement}
PRIMARY USER: {primary_user}
MARKET CONTEXT (TAM): {tam_estimate}

Return a JSON object with exactly these fields:

{{
  "methodology": "bottom-up or top-down — with a one-sentence explanation of which you used and why.",
  "tam": {{
    "value": "Dollar figure with units (e.g., '$9.4B')",
    "calculation": "Show the math step by step. Example: '47M users x $200 ARPU = $9.4B'",
    "assumptions": ["List each assumption as a separate string"]
  }},
  "sam": {{
    "value": "Dollar figure",
    "calculation": "How you narrowed from TAM to SAM",
    "rationale": "Why this segment and not others"
  }},
  "som": {{
    "value": "Dollar figure — what a realistic entrant could capture in 3 years",
    "calculation": "How you arrived at this number",
    "rationale": "What market dynamics support this capture rate"
  }},
  "beachhead_segment": "The specific, narrow first customer segment that would adopt fastest. Name them precisely.",
  "revenue_model_fit": "Which pricing model best fits this market and why: subscription, usage-based, transaction fee, or freemium.",
  "payback_intuition": "Given typical sales cycles and ARPU for this type of product, is this a quick-payback or long-payback business? One sentence.",
  "confidence": "high, medium, or low",
  "confidence_rationale": "One sentence explaining what drives uncertainty in this estimate."
}}
"""
    return call_gemini_json(prompt, SYSTEM)
