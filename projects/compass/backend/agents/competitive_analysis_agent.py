from .gemini_client import call_gemini_json

SYSTEM = """You are a competitive intelligence analyst who writes for product leaders making build-vs-buy decisions.
Name specific, real companies and products. Never use vague categories like 'large incumbents' or 'startups in this space'.
For each competitor, identify one specific gap — not a generic weakness.
If the input contains VERIFIED USER CLARIFICATIONS, the primary user and use case have been confirmed. Analyze competitors from that specific user's perspective — do not default to the most obvious or generic interpretation of the market.
Always output valid JSON only — no markdown, no explanation outside the JSON."""

def run(problem_statement: str, market_definition: str) -> dict:
    prompt = f"""
Analyze the competitive landscape for the following problem:

PROBLEM: {problem_statement}
MARKET: {market_definition}

Return a JSON object with exactly these fields:

{{
  "competitors": [
    {{
      "name": "Exact product name",
      "company": "Parent company name",
      "what_it_does": "One sentence describing what this product does, as a user would describe it.",
      "primary_strength": "The one thing this product does better than alternatives.",
      "critical_gap": "The one specific thing it cannot do that our problem requires.",
      "pricing_model": "How they charge. If unknown, say 'pricing not public'.",
      "target_customer": "Who this product is actually built for."
    }}
  ],
  "competitive_pattern": "One paragraph describing the dominant pattern in how incumbents approach this problem and why that creates an opening.",
  "differentiation_opportunity": "The specific, defensible angle an entrant could take based on these gaps. Be concrete.",
  "build_vs_buy_note": "Should a company entering this space build or buy? One sentence rationale."
}}

Include 3 to 5 real competitors. Prioritize the most relevant ones, not the most famous ones.
"""
    return call_gemini_json(prompt, SYSTEM)
