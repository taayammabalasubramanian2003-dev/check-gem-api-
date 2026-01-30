import streamlit as st
import google.generativeai as genai
import os

st.set_page_config(page_title="Gemini Test")

# Read API key from Streamlit Secrets
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ Gemini API key not found in Streamlit Secrets")
    st.stop()

# Configure Gemini
genai.configure(api_key=api_key)

# Use stable model
model = genai.GenerativeModel("models/gemini-1.5-flash")

st.title("🧪 Gemini API Test")

def ai_explain(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ Error: {e}"

st.success("✅ Gemini API key detected")

if st.button("Test Gemini"):
    st.write(ai_explain("Explain SIP investment in one simple line"))

