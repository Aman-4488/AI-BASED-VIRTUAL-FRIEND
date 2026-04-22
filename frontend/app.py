import sys
import os

# FIX: project root add to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import cv2
from deepface import DeepFace
from backend.suggestion_engine import get_suggestion

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

# ---------------- UI HOLDERS ----------------
frame_window = st.image([])

# ---------------- CAMERA ----------------
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

            # update only if emotion changes
            if emotion != st.session_state.emotion:
                st.session_state.emotion = emotion
                st.session_state.data = get_suggestion(emotion)

        except:
            pass

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_window.image(frame)

    cap.release()

# ---------------- SHOW UI (OUTSIDE LOOP) ----------------
if st.session_state.data:
    d = st.session_state.data

    st.markdown(f"### Emotion: **{st.session_state.emotion}**")
    st.write(d["message"])

    cols = st.columns(len(d["suggestions"]))

    for i, s in enumerate(d["suggestions"]):
        if cols[i].button(s, key=f"btn_{i}"):
            st.success(f"You selected: {s}")