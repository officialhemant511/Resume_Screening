import os
import json
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")

if not api_key:
    raise ValueError(
        "ANTHROPIC_API_KEY is missing. Check your .env file."
    )

client = Anthropic(api_key=api_key)


def analyze_job_description(job_description):

    prompt = f"""
Analyze the following job description and extract its requirements.

Return ONLY a valid JSON object.
Do not use markdown.
Do not use ```json.
Do not add any explanation before or after the JSON.

Use exactly this structure:

{{
    "skills": [],
    "requirements": [],
    "education": [],
    "experience": []
}}

Rules:

skills:
Include programming languages, frameworks, databases,
cloud technologies, tools and platforms explicitly mentioned.

requirements:
Include important technical responsibilities
and capabilities explicitly required.

education:
Include degree or education requirements explicitly mentioned.

experience:
Include required years or type of experience explicitly mentioned.

Do not invent requirements.

JOB DESCRIPTION:
{job_description}
"""

    response = client.messages.create(
        model="claude-sonnet-5",
        max_tokens=2000,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    # Extract Claude's text response
    text = ""

    for block in response.content:
        if block.type == "text":
            text += block.text

    text = text.strip()

    # Remove markdown code fences if Claude still returns them
    if text.startswith("```json"):
        text = text[7:]

    elif text.startswith("```"):
        text = text[3:]

    if text.endswith("```"):
        text = text[:-3]

    text = text.strip()

    try:
        return json.loads(text)

    except json.JSONDecodeError:
        print("\nClaude returned:\n")
        print(text)

        raise ValueError(
            "Claude did not return valid JSON. "
            "The raw response has been printed above."
        )