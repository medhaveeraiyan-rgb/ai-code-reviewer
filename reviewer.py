import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

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
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Please review this {language} code:\n\n{code}"}
        ],
        max_tokens=1500
    )
    return response.choices[0].message.content