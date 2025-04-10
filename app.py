import streamlit as st
import random
import datetime
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch

# Load empathetic chatbot model
tokenizer = AutoTokenizer.from_pretrained("microsoft/GODEL-v1_1-base-seq2seq")
model = AutoModelForSeq2SeqLM.from_pretrained("microsoft/GODEL-v1_1-base-seq2seq")

# Motivational quotes
quotes = [
    "You are stronger than you think.",
    "Take a deep breath. It's just a bad day, not a bad life.",
    "Keep going. You’ve got this!",
    "Be kind to yourself today.",
    "One step at a time is all it takes.",
    "Progress is progress, no matter how small.",
    "You don’t have to have it all figured out right now."
]

# Set up page
st.set_page_config(page_title="MindEase - Your AI Companion", layout="centered")
st.title("🧘‍♀️ MindEase - AI Mental Health Companion")

# --- Chatbot Section ---
st.subheader("💬 Talk to Your Companion")

user_input = st.text_input("How are you feeling today?", key="chat")

if user_input:
    with st.spinner("MindEase is responding..."):
        # Create prompt for GODEL
        prompt = f"Instruction: Respond with empathy and support.\nInput: {user_input}"
        input_ids = tokenizer(prompt, return_tensors="pt").input_ids

        # Generate response
        outputs = model.generate(input_ids, max_length=100)
        reply = tokenizer.decode(outputs[0], skip_special_tokens=True)
        st.success(reply)

# --- Mood Tracker Section ---
st.subheader("🌈 Mood Tracker")
mood = st.selectbox("Choose your current mood:", [
    "😊 Happy", "😔 Sad", "😠 Angry", "😌 Calm", "😩 Stressed", "😐 Neutral"
])

if st.button("Log Mood"):
    with open("mood_log.csv", "a", encoding="utf-8") as f:
        f.write(f"{datetime.datetime.now()},{mood}\n")
    st.success("Mood logged successfully!")

# --- Quote Section ---
st.subheader("💡 Today's Motivation")
st.info(random.choice(quotes))

# --- Journal Section ---
st.subheader("📝 Daily Journal")
journal_entry = st.text_area("Write something about your day...", height=150)

if st.button("Save Journal"):
    with open("journal.txt", "a", encoding='utf-8') as f:
        f.write(f"\n--- {datetime.datetime.now()} ---\n{journal_entry}\n")
    st.success("Journal entry saved!")