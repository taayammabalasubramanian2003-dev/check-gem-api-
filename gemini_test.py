import streamlit as st
import google.generativeai as genai
import os

# -----------------------------
# GEMINI SETUP (CORRECT)
# -----------------------------
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ Gemini API key not found. Add it to Streamlit Secrets.")
    st.stop()

genai.configure(api_key=api_key)

# ✅ USE ONLY THIS MODEL
model = genai.GenerativeModel("models/gemini-2.5-flash")

# -----------------------------
# AI EXPLANATION FUNCTION
# -----------------------------
def ai_explain(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ Gemini Error: {e}"
