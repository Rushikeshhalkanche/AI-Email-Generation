import os
from groq import Groq
from dotenv import load_dotenv
from app.prompt import BASIC_PROMPT, ADVANCED_PROMPT

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_email(intent, facts, tone, advanced=True):
    prompt_template = ADVANCED_PROMPT if advanced else BASIC_PROMPT

    prompt = prompt_template.format(
        intent=intent,
        facts="\n".join(facts),
        tone=tone
    )

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content