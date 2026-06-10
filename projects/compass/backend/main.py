from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ClarifyRequest(BaseModel):
    problem_statement: str

class DiscoveryRequest(BaseModel):
    problem_statement: str
    clarifications: List[str] = []  # user's answers to the clarification questions

class ImproveRequest(BaseModel):
    section_key: str
    original_content: dict
    eval_result: dict
    problem_statement: str

class ReadoutRequest(BaseModel):
    brief: dict
    synthesis: dict
    eval_scores: dict = {}

@app.post("/api/clarify")
async def clarify(request: ClarifyRequest):
    """
    Step 1: Read the problem statement and return an interpretation + clarifying questions.
    Fast — single Gemini call, no research agents.
    """
    if len(request.problem_statement) < 30:
        raise HTTPException(status_code=400, detail="Please describe your problem in more detail.")
    from agents.clarification_agent import run
    return run(request.problem_statement)

@app.post("/api/discover")
async def discover(request: DiscoveryRequest):
    """
    Step 2: Run the full discovery pipeline.
    If clarification answers were provided, they are woven into the problem statement
    so every agent has the full context.
    """
    if len(request.problem_statement) < 30:
        raise HTTPException(status_code=400, detail="Problem statement too short.")

    enriched = request.problem_statement
    if request.clarifications:
        answered = [a.strip() for a in request.clarifications if a.strip()]
        if answered:
            enriched = (
                "VERIFIED USER CLARIFICATIONS — treat these as authoritative facts. "
                "Do not contradict or override them with your own assumptions:\n"
                + "\n".join(f"- {a}" for a in answered)
                + "\n\nORIGINAL PROBLEM STATEMENT:\n"
                + request.problem_statement
            )

    from agents.orchestrator import run
    return await run(enriched)

@app.post("/api/improve")
async def improve(request: ImproveRequest):
    from agents.improve_agent import run as improve_run
    from agents.gemini_client import call_gemini_json
    from agents.eval_agent import RUBRIC

    improved = improve_run(
        section_key=request.section_key,
        original_content=request.original_content,
        eval_result=request.eval_result,
        problem_statement=request.problem_statement,
    )

    criteria = RUBRIC.get(request.section_key, [])
    new_eval = {}
    if criteria:
        prompt = f"""Score this rewritten section against the rubric.

SECTION: {request.section_key}
CONTENT: {improved}

RUBRIC (score each 0-10):
{chr(10).join(f"- {c}" for c in criteria)}

Return JSON:
{{
  "criteria_scores": [{{"criterion": "...", "score": 0-10, "reason": "one sentence"}}],
  "section_score": 0-100,
  "strongest_element": "...",
  "weakest_element": "...",
  "suggested_action": "..."
}}"""
        # Grading call — temperature=0 so re-scores are consistent with the original eval
        new_eval = call_gemini_json(prompt, "You are a CPO scoring a discovery brief section. Output valid JSON only.", temperature=0)

    return {"improved_content": improved, "new_eval": new_eval}

@app.post("/api/readout")
async def readout(request: ReadoutRequest):
    """
    Turn a completed discovery brief into an executive concept deck.
    One agent call — the frontend renders the returned slide JSON.
    """
    if not request.brief or not request.synthesis:
        raise HTTPException(status_code=400, detail="Run a discovery first — the readout is built from its results.")

    from agents.readout_agent import run as readout_run
    deck = readout_run(request.brief, request.synthesis, request.eval_scores)

    if deck.get("parse_error"):
        raise HTTPException(status_code=502, detail="The AI returned an unreadable deck. Please try again.")

    return {"deck": deck}

@app.get("/health")
async def health():
    return {"status": "healthy"}
