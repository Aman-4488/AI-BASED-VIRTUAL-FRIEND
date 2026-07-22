import sys
import os

# Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import cv2
from deepface import DeepFace
from database.db_manager import save_chat
from database.db_manager import initialize_db
from backend.ai_suggestion_engine import get_ai_suggestion
from backend.youtube_service import get_youtube_video
from backend.action_handler import handle_action
from utils.voice_input import listen_to_user
from backend.chat_engine import chat_with_ai
from database.db_manager import initialize_db, save_chat, save_mood
from frontend.components.header import render_header

# ---------- PARSE AI OUTPUT ----------
def parse_ai_output(text):
    lines = [l.strip() for l in text.split("\n") if l.strip()]

    message = lines[0] if len(lines) > 0 else ""

    suggestions = []
    if len(lines) > 1:
        suggestions = lines[1:3]

    return message, suggestions


initialize_db()
st.set_page_config(page_title="AI Virtual Friend", layout="centered")

render_header()

# ---------------- SESSION STATE ----------------
if "run" not in st.session_state:
    st.session_state.run = False

if "emotion" not in st.session_state:
    st.session_state.emotion = None

if "data" not in st.session_state:
    st.session_state.data = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "conversation" not in st.session_state:
    st.session_state.conversation = []

if "mood_history" not in st.session_state:
    st.session_state.mood_history = []

# ---------------- BUTTONS ----------------
col1, col2 = st.columns(2)

with col1:
    if st.button("▶️ Start"):
        st.session_state.run = True

with col2:
    if st.button("⏹️ Stop"):
        st.session_state.run = False

# ---------------- VOICE INPUT ----------------
st.write("---")

if st.button("🎤 Speak"):

    with st.spinner("Listening..."):

        voice_text = listen_to_user()

    st.success(f"You said: {voice_text}")

    # AI response
    with st.spinner("AI is thinking..."):

        ai_reply = get_ai_suggestion(voice_text)

    st.markdown("### 🤖 AI Reply")
    st.write(ai_reply)

# -----------------CHAT SECTION-----------------------------

# -----------------CHAT SECTION-----------------------------

st.write("---")
st.subheader("💬 Chat with AI")

user_message = st.text_input("Type your message")

if st.button("Send") and user_message:

    # Save user message in memory
    st.session_state.conversation.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    with st.spinner("AI is thinking..."):

        ai_reply = chat_with_ai(
            st.session_state.conversation
        )

    # Save AI reply in memory
    st.session_state.conversation.append(
        {
            "role": "assistant",
            "content": ai_reply
        }
    )

    # Show chat history
    st.session_state.chat_history.append(
        ("You", user_message)
    )

    st.session_state.chat_history.append(
        ("AI", ai_reply)
    )

    # Save chat to database
    save_chat("user", user_message)
    save_chat("assistant", ai_reply)

# Show only the latest conversation

st.write("---")

for sender, message in st.session_state.chat_history:

    if sender == "You":
        with st.chat_message("user"):
            st.write(message)

    else:
        with st.chat_message("assistant"):
            st.write(message)

            
st.subheader("📊 Mood Analytics")

if st.session_state.mood_history:

    mood_counts = {}

    for mood in st.session_state.mood_history:

        if mood not in mood_counts:
            mood_counts[mood] = 0

        mood_counts[mood] += 1

    st.write(mood_counts)

    most_common = max(
        mood_counts,
        key=mood_counts.get
    )

    st.success(
        f"Most Frequent Mood: {most_common}"
    )

# ---------------- CAMERA ----------------

frame_window = st.image([])

if st.session_state.run:
    cap = cv2.VideoCapture(0)

    while st.session_state.run:
        ret, frame = cap.read()

        if not ret:
            st.error("Camera not working")
            break

        try:
            result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
            emotion = result[0]['dominant_emotion']

            # update only when emotion changes
            if emotion != st.session_state.emotion:

                st.session_state.emotion = emotion

                # Save mood history
                st.session_state.mood_history.append(emotion)
                save_mood(emotion)
                print("Mood saved successfully")

                with st.spinner("Thinking..."):
                 st.session_state.data = get_ai_suggestion(emotion)

                print("AI DATA =", st.session_state.data)
        except Exception as e:
           print("ERROR:", e)
            

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_window.image(frame)

    cap.release()

# ---------------- DISPLAY AI OUTPUT ----------------
if st.session_state.data:
    ai_text = st.session_state.data

    message, suggestions = parse_ai_output(ai_text)

    st.markdown(
    f"""
    <div style="
        padding: 10px;
        border-radius: 10px;
        background-color: #1e1e1e;
        margin-top: 15px;
    ">
        <h3>🧠 Detected Emotion: {st.session_state.emotion}</h3>
    </div>
    """,
    unsafe_allow_html=True
)
    st.write(message)

    # अभी suggestions print करेंगे (buttons बाद में)
    st.write(" ")
    if suggestions:
        cols = st.columns(len(suggestions))
    
    for i, s in enumerate(suggestions):
        if cols[i].button(s, key=f"ai_btn_{i}"):
             st.success(f"Loading: {s}")

             video_url = get_youtube_video(s)

             if video_url:
               st.write("---")
               st.video(video_url)
             else:
                 st.error("Video not found") 