import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import datetime

# Set Streamlit config
st.set_page_config(page_title="MindEase", page_icon="🧠", layout="centered")

# Load model & tokenizer
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

# App title
st.title("🧘 MindEase - Your AI Mood Companion")

# Instructions
st.markdown("Hello there! 👋 I'm here to listen. Share how you're feeling today and I'll chat with you.")

# Mood input
mood = st.text_input("💬 What's on your mind?")

# Process response
if mood:
    with st.spinner("Thinking..."):
        input_ids = tokenizer.encode(mood + tokenizer.eos_token, return_tensors='pt')
        output_ids = model.generate(
            input_ids,
            max_length=1000,
            pad_token_id=tokenizer.eos_token_id,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            temperature=0.7
        )
        reply = tokenizer.decode(output_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)

        # Show reply
        st.markdown(f"🧠 **MindEase says:** {reply}")

        # Save to log file
        try:
            with open("mood_log.csv", "a", encoding="utf-8") as f:
                f.write(f"{datetime.datetime.now()},{mood},{reply}\n")
        except Exception as e:
            st.error("⚠️ Could not log your entry. Error: " + str(e))

        # Reassurance
        st.success("You're doing great — remember to take care of yourself 💙")

# Footer
st.markdown("---")
st.caption("Made with 💖 using Streamlit & Hugging Face Transformers")
