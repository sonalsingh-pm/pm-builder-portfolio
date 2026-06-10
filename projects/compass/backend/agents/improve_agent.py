"""
Improve Agent — the feedback loop.

Called when a user clicks 'Improve' on a low-scoring section.
Takes the original section content, the eval weakness, and the suggested action,
then rewrites the section addressing those specific gaps.

This demonstrates the eval-then-improve loop:
  Write -> Score -> Identify weakness -> Rewrite with weakness in prompt -> Re-score
"""

from .gemini_client import call_gemini_json

SYSTEM = """You are a senior product strategist rewriting a section of a discovery brief.
A PM-written eval rubric identified specific weaknesses in the previous version.
Your job is to produce a materially better version that addresses those weaknesses.
Keep the same JSON structure as the original. Do not add fields or remove fields.
Always output valid JSON only — no markdown, no explanation outside the JSON."""

def run(section_key: str, original_content: dict, eval_result: dict, problem_statement: str) -> dict:
    weakness = eval_result.get("weakest_element", "")
    suggested_action = eval_result.get("suggested_action", "")
    score = eval_result.get("section_score", 0)
    criteria = eval_result.get("criteria_scores", [])

    low_criteria = [c for c in criteria if c.get("score", 10) < 7]

    prompt = f"""
You are rewriting the {section_key.replace("_", " ")} section of a product discovery brief.

ORIGINAL PROBLEM STATEMENT: {problem_statement}

ORIGINAL CONTENT:
{original_content}

EVAL FEEDBACK (previous version scored {score}/100):
- Weakest element: {weakness}
- Suggested action: {suggested_action}
- Specific criteria that scored below 7/10:
{chr(10).join(f"  - {c.get('criterion', '')}: {c.get('score', 0)}/10 — {c.get('reason', '')}" for c in low_criteria)}

Rewrite this section to directly address each weakness above.
The rewritten version must have the same JSON field names as the original.
Return only the improved JSON object for the {section_key.replace("_", " ")} section.
"""
    return call_gemini_json(prompt, SYSTEM)
