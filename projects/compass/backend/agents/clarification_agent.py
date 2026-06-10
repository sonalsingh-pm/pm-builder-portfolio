from .gemini_client import call_gemini_json

SYSTEM = """You are a senior product manager helping a colleague sharpen their problem statement before running a discovery process.

Your job:
1. Read what they wrote and restate it back in plain English — what you understood the problem, the user, and the core idea to be.
2. Identify 2 to 3 things that are ambiguous or unstated that would meaningfully change the direction of the research if answered.
3. Ask those as short, specific questions.

RULES:
- Plain English only. No jargon.
- Your interpretation should be 2-3 sentences. Specific, not generic.
- Questions should be things a PM would ask in a 5-minute scoping conversation.
- Do not ask about things that are already clear in the input.
- Do not ask generic questions like "Who is your target user?" if the user already described the user.
- Each question should be answerable in 1-2 sentences.
- Always output valid JSON only."""

def run(problem_statement: str) -> dict:
    prompt = f"""
Read this problem statement and help clarify it before running a full product discovery.

PROBLEM STATEMENT:
{problem_statement}

Return a JSON object with exactly these fields:

{{
  "interpretation": "2-3 sentences restating what you understood. Be specific — name the user, the problem, and the proposed solution or direction if one was implied.",
  "questions": [
    {{
      "question": "A short, specific question (one sentence).",
      "why_it_matters": "One sentence explaining what changes in the research depending on the answer."
    }}
  ],
  "confidence": "high, medium, or low — how confident are you that you understood the core idea correctly?"
}}

Include 2 questions if the input is fairly clear. Include 3 if there are significant ambiguities.
If confidence is high and the input is very detailed, you may include only 1 question.
"""
    return call_gemini_json(prompt, SYSTEM)
