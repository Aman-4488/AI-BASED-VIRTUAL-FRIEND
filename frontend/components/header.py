import streamlit as st

def render_header():
    st.markdown(
    """
    <h1 style='text-align: center; color: #4CAF50;'>
        🤖 AI Virtual Friend
    </h1>
    <p style='text-align: center;'>
        Your smart mood-based AI companion
    </p>
    <hr>
    """,
    unsafe_allow_html=True
)

