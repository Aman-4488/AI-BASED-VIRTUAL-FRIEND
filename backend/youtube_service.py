import os
import requests
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")

def get_youtube_video(query):
    url = "https://www.googleapis.com/youtube/v3/search"

    params = {
        "part": "snippet",
        "q": query,
        "key": API_KEY,
        "maxResults": 1,
        "type": "video"
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if "items" in data and len(data["items"]) > 0:
            video_id = data["items"][0]["id"]["videoId"]
            return f"https://www.youtube.com/watch?v={video_id}"

    except Exception as e:
        print("YouTube API Error:", e)

    return None