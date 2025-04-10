import streamlit as st
import datetime
import os

# Title
st.title("🧠 MindEase: Your Mood Companion")

# Mood options
mood = st.radio("How are you feeling today?", ["😊 Happy", "😞 Sad", "😠 Angry", "😨 Anxious", "😐 Neutral"])

# Display emoji feedback
st.write(f"Thanks for sharing your mood: {mood}")

# Optional reflection input
reflection = st.text_area("Want to talk about it?")

# Save mood log
if st.button("Save my mood"):
    with open("mood_log.csv", "a", encoding="utf-8") as f:
        f.write(f"{datetime.datetime.now()},{mood},{reflection}\n")
    st.success("Mood saved successfully! ✅")

# AI Companion Logic
def get_response(user_input):
    if "sad" in user_input.lower():
        return "I'm really sorry you're feeling this way. Want to share more?"
    elif "happy" in user_input.lower():
        return "That's awesome! Keep smiling and spread the joy 😊"
    elif "angry" in user_input.lower():
        return "Take a deep breath. I'm here to listen."
    elif "anxious" in user_input.lower():
        return "It's okay to feel anxious. Let's talk about what's bothering you."
    else:
        return "I'm always here to chat whenever you want."

# Chat section
st.subheader("🗨️ Chat with MindEase")

chat_input = st.text_input("Type something you'd like to share...")
if chat_input:
    response = get_response(chat_input)
    st.markdown(f"**MindEase:** {response}")
