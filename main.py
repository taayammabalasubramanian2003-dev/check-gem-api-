import streamlit as st
import google.generativeai as genai
import os

st.set_page_config(page_title="Gemini API Test", layout="centered")
st.title("🧪 Gemini API Test")

# Load API Key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ Gemini API key not found in Streamlit Secrets")
    st.stop()

# Configure Gemini
genai.configure(api_key=api_key)

# ✅ CORRECT MODEL
model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

def ai_explain(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ Error: {e}"

st.success("✅ Gemini API key detected")

st.subheader("🔍 Test Output")
st.write(ai_explain("Explain investing to a beginner in one sentence"))

