import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def chat_with_ai(chat_history):

    try:

        messages = [
            {
                "role": "system",
                "content": "You are a friendly AI virtual friend."
            }
        ]

        messages.extend(chat_history)

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {e}"