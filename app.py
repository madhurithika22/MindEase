import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import datetime

# Load DialoGPT model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

# App UI
st.set_page_config(page_title="MindEase", page_icon="🧠", layout="centered")
st.title("🧘 MindEase: Your AI Mood Companion")

st.write("Hello! I'm here to talk with you. How are you feeling today?")

# Input box
mood = st.text_input("💬 Share your mood or thoughts here:")

if mood:
    with st.spinner("Thinking..."):
        # Encode user input and generate a response
        input_ids = tokenizer.encode(mood + tokenizer.eos_token, return_tensors='pt')
        output_ids = model.generate(input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
        reply = tokenizer.decode(output_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)

        # Display AI response
        st.markdown(f"🧠 **MindEase says:** {reply}")

        # Save the conversation (for local logging)
        with open("mood_log.csv", "a", encoding="utf-8") as f:
            f.write(f"{datetime.datetime.now()},{mood},{reply}\n")

        # Optional: positive feedback message
        st.success("You're not alone. MindEase is always here for you 💙")

# Footer
st.markdown("---")
st.markdown("Made with 💖 using Streamlit and Hugging Face Transformers")
