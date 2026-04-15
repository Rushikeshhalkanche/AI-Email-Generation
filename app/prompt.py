BASIC_PROMPT = """
Write a professional email.

Intent: {intent}
Facts: {facts}
Tone: {tone}
"""

ADVANCED_PROMPT = """
You are a professional email assistant.

Generate a high-quality email.

Intent: {intent}

Key Facts:
{facts}

Tone: {tone}

Rules:
- Include ALL facts clearly
- Maintain tone strictly
- Use proper greeting and closing
- Keep it concise

Example:
Intent: Follow up
Facts:
- Discussed timeline
- Need approval
Tone: formal

Output:
Dear Sir,
...

Now generate the email:
"""