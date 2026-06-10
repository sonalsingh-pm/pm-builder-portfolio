from google import genai
from google.genai import types
import os, json, re, time, threading

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Wider fallback list — if flash models are all overloaded, pro models may still respond
MODELS = [
    "gemini-flash-lite-latest",
    "gemini-2.0-flash-lite",
    "gemini-2.0-flash-001",
    "gemini-flash-latest",
    "gemini-pro-latest",
    "gemini-2.0-flash",
]

EMBEDDING_MODEL = "models/gemini-embedding-001"

# Semaphore: max 2 simultaneous Gemini calls so we don't trigger free-tier throttling
_semaphore = threading.Semaphore(2)

def call_gemini(prompt: str, system_context: str = "", json_mode: bool = False, temperature: float = None) -> str:
    full_prompt = f"{system_context}\n\n{prompt}" if system_context else prompt
    last_error = None

    # json_mode forces the model to emit syntactically valid JSON — it cannot
    # add chatter like "Sure! Here's your JSON:" that breaks the parser.
    # temperature=0 makes output deterministic — used for grading/eval calls.
    config_kwargs = {}
    if json_mode:
        config_kwargs["response_mime_type"] = "application/json"
    if temperature is not None:
        config_kwargs["temperature"] = temperature
    config = types.GenerateContentConfig(**config_kwargs) if config_kwargs else None

    with _semaphore:
        for model in MODELS:
            for attempt in range(3):
                try:
                    response = client.models.generate_content(
                        model=model,
                        contents=full_prompt,
                        config=config,
                    )
                    return response.text

                except Exception as e:
                    last_error = e
                    err = str(e)

                    if "503" in err or "UNAVAILABLE" in err:
                        if attempt < 2:
                            time.sleep((2 ** attempt) * 3)  # 3s, then 6s
                        continue

                    elif "429" in err or "RESOURCE_EXHAUSTED" in err:
                        break  # quota hit — try next model

                    elif "404" in err or "NOT_FOUND" in err:
                        break  # model not available — try next model

                    else:
                        raise

    raise Exception(
        f"All Gemini models are currently unavailable (Google service issue). "
        f"Please wait a few minutes and try again. Last error: {str(last_error)[:120]}"
    )

def call_gemini_json(prompt: str, system_context: str = "", temperature: float = None) -> dict:
    raw = call_gemini(prompt, system_context, json_mode=True, temperature=temperature)
    cleaned = re.sub(r"```json\s*|\s*```", "", raw).strip()
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        return {"raw_text": raw, "parse_error": True}

def embed_text(text: str) -> list:
    result = client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=text,
    )
    return result.embeddings[0].values
