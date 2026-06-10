from .gemini_client import call_gemini_json

SYSTEM = """You are a market analyst who writes for senior product and strategy leaders.
Your job is to produce directionally accurate market framing based on your training knowledge — not invented statistics.

RULES:
- You do not have internet access. Do not invent citations or fabricate source names.
- For any number you include, label it clearly: [Well-known estimate] for figures that are publicly established, [Estimated] for your own reasoning, or [Assumption] for things you are inferring.
- It is better to say "this market is estimated to be in the low billions based on [reasoning]" than to invent a precise figure with a fake citation.
- If the input contains VERIFIED USER CLARIFICATIONS, those facts define the user and problem. Do not contradict them.
Always output valid JSON only — no markdown, no explanation outside the JSON."""

def run(problem_statement: str, reframed_problem: str) -> dict:
    prompt = f"""
Research the market for the following product problem:

PROBLEM: {problem_statement}
REFRAMED: {reframed_problem}

Return a JSON object with exactly these fields:

{{
  "market_definition": "One sentence defining the specific market this product competes in.",
  "tam_estimate": "Total Addressable Market in dollars. Show your math. Example: '47M knowledge workers in US x $200/year = $9.4B TAM'. Label assumptions.",
  "tam_source": "Source or methodology for the TAM estimate. If assumed, say so explicitly.",
  "growth_rate": "Annual growth rate of this market with source.",
  "growth_driver": "The primary force driving this growth. Be specific — not 'digital transformation'.",
  "market_maturity": "One of: emerging, growing, mature, declining. With a one-sentence justification.",
  "key_trends": [
    "Trend 1: specific description with recency indicator",
    "Trend 2: specific description",
    "Trend 3: specific description"
  ],
  "analogous_markets": "One or two markets that have already gone through a similar shift. What can we learn from them?",
  "data_confidence": "high, medium, or low — with a one-sentence explanation of why."
}}
"""
    return call_gemini_json(prompt, SYSTEM)
