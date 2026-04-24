import webbrowser
from backend.youtube_service import get_youtube_video

def handle_action(text):
    query = text

    # YouTube API call
    video_url = get_youtube_video(query)

    if video_url:
        webbrowser.open(video_url)
    else:
        # fallback
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")