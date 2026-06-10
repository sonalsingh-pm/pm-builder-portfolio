from .gemini_client import call_gemini_json

SYSTEM = """You are a senior product strategist with deep expertise in the Jobs-To-Be-Done framework.
Your job is to take a raw problem statement from a product manager and produce a rigorous, structured JTBD analysis.
Be specific. Use real language. Never use phrases like 'seamless experience' or 'innovative solution'.

CRITICAL RULE: If the input contains a section labeled "VERIFIED USER CLARIFICATIONS," those are facts the PM has confirmed. Your primary_user and reframed_problem must reflect them exactly. Do not override clarified facts with your own interpretation. If the PM said their primary user is people who struggle with sweet tooth cravings, your primary_user must be those people — not athletes, not health enthusiasts in general.

Always output valid JSON only — no markdown, no explanation outside the JSON."""

def run(problem_statement: str) -> dict:
    prompt = f"""
Analyze this problem statement using the Jobs-To-Be-Done framework:

PROBLEM STATEMENT: {problem_statement}

Return a JSON object with exactly these fields:

{{
  "primary_user": "One specific sentence describing who this user is. Include role, context, seniority if relevant.",
  "jtbd_statement": "When [situation], this user wants to [motivation], so they can [expected outcome].",
  "functional_outcome": "The practical, measurable thing the user needs to accomplish.",
  "emotional_outcome": "How the user wants to feel during or after accomplishing this.",
  "social_outcome": "How the user wants to be perceived by others (manager, team, stakeholders) as a result.",
  "current_struggle": "One paragraph describing exactly where the current approach breaks down. Be specific.",
  "reframed_problem": "A cleaner, more precise version of the problem statement that captures the real need. 2-3 sentences.",
  "is_solution_disguised_as_problem": true or false,
  "solution_reframe_note": "If is_solution_disguised_as_problem is true, explain the reframe here. Otherwise empty string."
}}
"""
    return call_gemini_json(prompt, SYSTEM)
