"""
Internal Search Agent — Phase 1 of the Compass pipeline.

This agent searches the user's internal knowledge base (stored in Pinecone as embeddings)
before launching external research. This implements the RAG pattern:
- Documents from Notion are embedded and stored in Pinecone
- This agent queries Pinecone to find semantically similar past work
- Returns one of three outcomes: nothing found, prior work found, active project found

For this MVP, if Pinecone is not configured or has no documents, returns 'no_prior_work'.
"""

import os
from .gemini_client import call_gemini_json, embed_text

def run(problem_statement: str) -> dict:
    """
    Search Pinecone for documents related to this problem statement.
    Returns a dict with status and any relevant prior work found.
    """
    pinecone_key = os.getenv("PINECONE_API_KEY", "")

    if not pinecone_key or pinecone_key == "your-pinecone-api-key-here":
        return {
            "status": "no_prior_work",
            "message": "No internal knowledge base configured.",
            "documents": []
        }

    try:
        from pinecone import Pinecone

        pc = Pinecone(api_key=pinecone_key)
        index = pc.Index("compass-kb")

        # Embed the problem statement to find semantically similar documents
        query_vector = embed_text(problem_statement)

        # Search for top 3 most similar documents
        results = index.query(
            vector=query_vector,
            top_k=3,
            include_metadata=True
        )

        matches = results.get("matches", [])
        if not matches or matches[0]["score"] < 0.75:
            return {
                "status": "no_prior_work",
                "message": "No closely related internal documents found.",
                "documents": []
            }

        # Found relevant documents — classify them
        docs = [
            {
                "title": m["metadata"].get("title", "Untitled"),
                "summary": m["metadata"].get("summary", ""),
                "status": m["metadata"].get("status", "unknown"),
                "owner": m["metadata"].get("owner", ""),
                "similarity_score": round(m["score"], 3),
                "source": m["metadata"].get("source", "internal")
            }
            for m in matches
        ]

        # Check if any document represents an active project
        active = [d for d in docs if d["status"] == "active"]
        if active:
            return {
                "status": "active_project",
                "message": f"An active project already exists covering this area: '{active[0]['title']}'. Owner: {active[0]['owner']}.",
                "documents": docs
            }

        return {
            "status": "prior_work_found",
            "message": f"Found {len(docs)} related internal document(s). Incorporating into research.",
            "documents": docs
        }

    except Exception as e:
        # Don't crash the pipeline if RAG fails — just proceed without internal context
        return {
            "status": "no_prior_work",
            "message": f"Internal search unavailable: {str(e)}",
            "documents": []
        }
