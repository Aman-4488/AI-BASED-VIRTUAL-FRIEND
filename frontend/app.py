import sys
import os

# Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import cv2
from deepface import DeepFace
from backend.ai_suggestion_engine import get_ai_suggestion
from backend.action_handler import handle_action

# ---------- PARSE AI OUTPUT ----------
def parse_ai_output(text):
    lines = [l.strip() for l in text.split("\n") if l.strip()]

    message = lines[0] if len(lines) > 0 else ""

    suggestions = []
    if len(lines) > 1:
        suggestions = lines[1:3]

    return message, suggestions

st.set_page_config(page_title="AI Virtual Friend", layout="centered")

st.title("🤖 AI Virtual Friend")

# ---------------- SESSION STATE ----------------
if "run" not in st.session_state:
    st.session_state.run = False

if "emotion" not in st.session_state:
    st.session_state.emotion = None

if "data" not in st.session_state:
    st.session_state.data = None

# ---------------- BUTTONS ----------------
col1, col2 = st.columns(2)

with col1:
    if st.button("▶️ Start"):
        st.session_state.run = True

with col2:
    if st.button("⏹️ Stop"):
        st.session_state.run = False

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
                st.session_state.data = get_ai_suggestion(emotion)

        except:
            pass

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_window.image(frame)

    cap.release()

# ---------------- DISPLAY AI OUTPUT ----------------
if st.session_state.data:
    ai_text = st.session_state.data

    message, suggestions = parse_ai_output(ai_text)

    st.markdown(f"### Emotion: **{st.session_state.emotion}**")
    st.write(message)

    # अभी suggestions print करेंगे (buttons बाद में)
    if suggestions:
        cols = st.columns(len(suggestions))
    
    for i, s in enumerate(suggestions):
        if cols[i].button(s, key=f"ai_btn_{i}"):
            st.success(f"Opening: {s}")
            handle_action(s)