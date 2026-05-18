import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_ai_suggestion(emotion):
    prompt = f"""
    The user is feeling {emotion}.
    
    Give:
    - A short friendly message
    - 2 helpful suggestions
    
    Keep response short and clean.
    """

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",   # ✅ FIXED MODEL
            messages=[
                {"role": "system", "content": "You are a friendly AI assistant."},
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"