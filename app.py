import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Page Config
st.set_page_config(page_title="PhishGuard AI", page_icon="🛡️")

# Sidebar for Setup
st.sidebar.title("Configuration")

# Try to load API key from .env file first, otherwise ask user
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')

    st.title("🛡️ PhishGuard AI Analyzer")
    st.write("Paste the content of a suspicious email below to analyze it for phishing threats.")

    # Input Area
    email_content = st.text_area("Email Body Content:", height=200, placeholder="Dear User, your account has been compromised...")

    if st.button("Run Security Analysis"):
        if email_content:
            with st.spinner("Analyzing email patterns..."):
                # The Security Prompt
                prompt = f"Act as a Cyber Security Analyst. Analyze this email for phishing. Give a Risk Score (0-10) and list Red Flags: {email_content}"
                
                response = model.generate_content(prompt)
                
                # Display Results
                st.subheader("Analysis Report")
                st.markdown(response.text)
        else:
            st.warning("Please paste an email first!")
else:
    st.info("Please enter your API Key in the sidebar to start.")