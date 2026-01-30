import streamlit as st
import google.generativeai as genai
import os

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(page_title="Gemini Test", layout="centered")
st.title("🧪 Gemini API Test")

# -------------------------
# LOAD API KEY
# -------------------------
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ Gemini API key not found in Streamlit Secrets")
    st.stop()

st.success("✅ Gemini API key detected")

# -------------------------
# GEMINI CONFIG
# -------------------------
genai.configure(api_key=api_key)
model = genai.GenerativeModel("models/gemini-pro")

# -------------------------
# AI FUNCTION (DEFINE FIRST)
# -------------------------
def ai_explain(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ Gemini Error: {e}"

# -------------------------
# TEST PROMPTS
# -------------------------
st.subheader("🔍 Simple Test")
st.write(ai_explain("Say hello in one sentence"))

st.subheader("📘 Finance Test")
st.write(ai_explain("Explain what RSI means to a beginner investor in one line"))

st.subheader("📈 Stock Test")
st.write(ai_explain("Explain whether TCS stock is good for long-term investment in simple words"))
