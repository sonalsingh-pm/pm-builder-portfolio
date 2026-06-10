"""
Run this once to find which Gemini model works with your API key.
It automatically updates gemini_client.py with the working model.
"""
from google import genai
import os, re
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

candidates = [
    "gemini-2.0-flash-lite",
    "gemini-2.0-flash",
    "gemini-flash-lite-latest",
    "gemini-flash-latest",
    "gemini-2.5-flash",
    "gemini-pro-latest",
]

print("Testing models...\n")
working = None
for model in candidates:
    try:
        r = client.models.generate_content(model=model, contents="Reply with one word: ready")
        print(f"  WORKS: {model}  ({r.text.strip()})")
        working = model
        break
    except Exception as e:
        msg = str(e)[:120].replace("\n", " ")
        print(f"  FAIL:  {model}  — {msg}")

if working:
    path = "agents/gemini_client.py"
    with open(path) as f:
        content = f.read()
    content = re.sub(r'MODEL = "[^"]*"', f'MODEL = "{working}"', content)
    with open(path, "w") as f:
        f.write(content)
    print(f"\nDone. gemini_client.py updated to use: {working}")
    print("Start the server: uvicorn main:app --reload")
else:
    print("\nNo model worked. Your API key may need billing enabled at aistudio.google.com")
