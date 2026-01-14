import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

# Add validation to ensure API key is loaded
if not API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in .env file. Please create a .env file with your API key.")

genai.configure(api_key=API_KEY)

def analyze_email_for_phishing(email_text):
    
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    
    prompt = f"""
    Act as a Senior Cyber Security Analyst. Analyze the following email content for phishing risks.
    
    Look specifically for:
    - Urgency or threats (e.g., "Account will be deleted")
    - Deceptive links or strange domains
    - Unusual requests (e.g., asking for gift cards or passwords)
    - Grammatical errors or "weird" tone
    
    Return your report in this format:
    ---
    Analyze this email for phishing. You MUST respond in exactly 4 lines using this template:
    Line 1: SCORE: [0-10]/10
    Line 2: VERDICT: [Safe/Suspicious/Malicious]
    Line 3: REASON: [One sentence explaining the biggest red flag]
    Line 4: ACTION: [One short instruction for the user]
    ---
    
    EMAIL CONTENT TO ANALYZE:
    {email_text}
    """
    
    response = model.generate_content(prompt)
    return response.text

# 4. TEST IT: Paste a suspicious email here to test
sample_email = """
From: support@secure-bank-login.net
Subject: UNUSUAL LOGIN DETECTED!
Your account was accessed from Russia. If this was not you, click here to 
verify your identity immediately or your funds will be frozen: 
http://bit.ly/secure-verify-99
"""

if __name__ == "__main__":
    print("--- AI PHISHING ANALYSIS REPORT ---")
    print(analyze_email_for_phishing(sample_email))