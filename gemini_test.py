import streamlit as st
import google.generativeai as genai
import os

st.title("🧪 Gemini API Test")

# 1. Load API Key Securely
try:
    api_key = st.secrets["GEMINI_API_KEY"]
except (FileNotFoundError, KeyError):
    api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ GEMINI_API_KEY not found. Please set it in .streamlit/secrets.toml")
    st.stop()

# 2. Configure Gemini
genai.configure(api_key=api_key)

# ✅ UPDATED TO YOUR WORKING MODEL
model = genai.GenerativeModel("models/gemini-2.5-flash")

def ai_explain(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ Error: {e}"

st.success("✅ Gemini API key detected & Model Connected")

st.subheader("🔍 Test Output")
if st.button("Run Explanation"):
    with st.spinner("Generating..."):
        result = ai_explain("Explain investing to a beginner in one simple line")
        st.write(result)
