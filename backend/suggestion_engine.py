def get_suggestion(emotion):

    if emotion == "happy":
        return {
            "message": "You look happy 😄",
            "suggestions": ["Listen to music 🎵", "Watch funny video 😂"]
        }

    elif emotion == "sad":
        return {
            "message": "Hey, you seem sad 😢",
            "suggestions": ["Watch motivational video 🎥", "Talk to me 💬"]
        }

    elif emotion == "angry":
        return {
            "message": "Take a breath 😌",
            "suggestions": ["Calm music 🎵", "Meditation 🧘"]
        }

    else:
        return {
            "message": "How are you feeling?",
            "suggestions": ["Chat 💬", "Explore something new 🚀"]
        }