import streamlit as st
import google.generativeai as genai
import os

st.title("🧪 Gemini API Test")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ Gemini API key not found in Streamlit Secrets")
    st.stop()

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.0-pro")

def ai_explain(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ Error: {e}"

st.success("✅ Gemini API key detected")
st.write(ai_explain("Explain investing to a beginner in one line"))
