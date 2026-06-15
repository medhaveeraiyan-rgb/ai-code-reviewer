import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
MAX_CODE_CHARS = int(os.getenv("MAX_CODE_CHARS", "8000"))

MODEL_NAME = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
import streamlit as st

_api_key = (
    st.secrets.get("GROQ_API_KEY")
    or os.getenv("GROQ_API_KEY")
)

if not _api_key:
    raise EnvironmentError(
        "GROQ_API_KEY is not set. "
        "Please configure it in Streamlit secrets or .env"
    )

client = Groq(api_key=_api_key)

SYSTEM_PROMPT = """You are a senior software engineer
doing a thorough code review.

For every issue you find:
1. State the line number (if visible)
2. Explain clearly WHY it is a problem
3. Show a corrected version of the code

Cover these areas:
- Bugs (things that will break or crash)
- Security (e.g. SQL injection, exposed secrets)
- Performance (slow or wasteful code)
- Style (naming, readability, best practices)

Format your response in clear sections.
Use simple English — the developer is a beginner."""

def review_code(code: str, language: str) -> str:
    if not code or not code.strip():
        return "⚠️ No code provided. Please paste some code first."

    if len(code) > MAX_CODE_CHARS:
        return (
            f"⚠️ Code is too long ({len(code):,} characters). "
            f"Please keep it under {MAX_CODE_CHARS:,} characters "
            f"for a focused review."
        )

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {
                    "role": "user",
                    "content": f"Please review this {language} code:\n\n{code}"
                }
            ],
            max_tokens=1500,
        )

        return response.choices[0].message.content

    except Exception as e:
        error_type = type(e).__name__

        return (
            f"⚠️ Review failed ({error_type})\n\n"
            f"Something went wrong while contacting the AI.\n"
            f"Please check your API key and try again.\n\n"
            f"Technical detail: {str(e)}"
        )