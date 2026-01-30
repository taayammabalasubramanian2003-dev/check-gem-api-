import streamlit as st
import google.generativeai as genai
import os

# ---------------------------
# PAGE SETUP
# ---------------------------
st.set_page_config(page_title="Gemini API Test", layout="centered")
st.title("🧪 Gemini API Test")

# ---------------------------
# API KEY CHECK
# ---------------------------
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ Gemini API key not found. Add it in Streamlit Secrets.")
    st.stop()

st.success("✅ Gemini API key detected")

# ---------------------------
# GEMINI CONFIG
# ---------------------------
genai.configure(api_key=api_key)

# ✅ USE ONLY THIS MODEL
model = genai.GenerativeModel("gemini-pro")

# ---------------------------
# AI FUNCTION
# ---------------------------
def ai_explain(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ Error: {e}"

# ---------------------------
# TEST BUTTON
# ---------------------------
if st.button("Test Gemini"):
    result = ai_explain("Say hello to a beginner investor in one sentence.")
    st.write(result)
