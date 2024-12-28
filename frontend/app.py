import streamlit as st
import requests

# Streamlit app configuration
st.set_page_config(page_title="Multilingual Chatbot", layout="wide")

# API endpoint
API_URL = "http://127.0.0.1:8000/chat"

# Language options
languages = {
    "English": "en",
    "Hindi": "hi",
    "Marathi": "mr",
    "Gujarati": "guw",
}

# Chat UI
st.title("🤖 Multilingual Chatbot")
st.write("Select a language and start chatting with the bot!")

language = st.selectbox("Choose your language:", options=list(languages.keys()))
user_input = st.text_input("You:", key="user_input")

if st.button("Send"):
    if user_input:
        # Send input to backend
        response = requests.post(
            API_URL,
            json={"message": user_input, "language": languages[language]},
        )
        if response.status_code == 200:
            bot_response = response.json()["response"]
            st.text_area("Bot:", value=bot_response, height=100, key="bot_response")
        else:
            st.error("Error communicating with the chatbot backend.")
    else:
        st.warning("Please enter a message.")

# Footer
st.markdown("**Developed by [Your Name]**")
