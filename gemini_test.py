import streamlit as st
import google.generativeai as genai
import os

st.set_page_config(page_title="Gemini Version Checker", page_icon="🕵️")

st.title("🕵️ Gemini Model Version Checker")
st.write("This tool tests which model names connect successfully with your API key.")

# --- 1. SETUP API KEY ---
try:
    # Try getting key from secrets first
    api_key = st.secrets["GEMINI_API_KEY"]
except (FileNotFoundError, KeyError):
    # Fallback to environment variable
    api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ API Key not found. Please set GEMINI_API_KEY in .streamlit/secrets.toml")
    st.stop()

genai.configure(api_key=api_key)
st.success("✅ API Key Authentication Successful")

# --- 2. DEFINE TEST FUNCTION ---
def test_model_connection(model_name):
    """Attempts to generate a simple response from a specific model."""
    try:
        model = genai.GenerativeModel(model_name)
        # We generate a tiny prompt to save quota and speed up the test
        response = model.generate_content("Hi", request_options={"timeout": 5})
        return True, "Working"
    except Exception as e:
        return False, str(e)

# --- 3. AUTO-DISCOVERY (Ask Google what we have) ---
st.subheader("1. Models allocated to your Key")
st.write("Querying Google for your available list...")

found_working_model = False
available_models = []

try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            available_models.append(m.name)
except Exception as e:
    st.error(f"Could not list models: {e}")

if available_models:
    for model_name in available_models:
        success, message = test_model_connection(model_name)
        if success:
            st.success(f"✅ **{model_name}** is WORKING")
            found_working_model = True
        else:
            st.warning(f"⚠️ {model_name} found but failed: {message}")
else:
    st.warning("No models returned by list_models(). Trying manual list below...")

# --- 4. MANUAL CHECK (Force test common aliases) ---
st.subheader("2. Testing Common Model Aliases")
st.write("Testing standard aliases often used in tutorials...")

# List of common aliases to force-check
common_aliases = [
    "gemini-2.0-flash-exp",
    "gemini-1.5-flash",
    "gemini-1.5-flash-latest",
    "gemini-1.5-pro",
    "gemini-1.5-pro-latest",
    "gemini-pro",
    "models/gemini-1.5-flash", # Explicit prefix
]

for alias in common_aliases:
    # Skip if we already checked it in step 1
    if alias in available_models or f"models/{alias}" in available_models:
        continue
        
    success, message = test_model_connection(alias)
    if success:
        st.success(f"✅ **{alias}** is WORKING")
        st.code(f'model = genai.GenerativeModel("{alias}")', language="python")
    else:
        # Just show a small text for failures to keep it clean
        st.caption(f"❌ {alias}: {message.split('404')[0] if '404' in message else 'Failed'}")

st.divider()
st.info("💡 **Tip:** Copy the green model name above and paste it into your original app code.")
