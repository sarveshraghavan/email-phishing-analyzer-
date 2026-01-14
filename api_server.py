from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

app = Flask(__name__)
CORS(app) # This allows the browser extension to talk to this script

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    email_text = data.get('content', '')
    
    # Use the 4-line prompt we built earlier
    model = genai.GenerativeModel('gemini-2.5-flash')
    prompt = f"Analyze this email for phishing. Respond in exactly 4 lines (Score, Verdict, Reason, Action): {email_text}"
    
    response = model.generate_content(prompt)
    
    # Return as JSON so the extension can read it easily
    return jsonify({"analysis": response.text})

if __name__ == '__main__':
    app.run(port=5000, debug=True)