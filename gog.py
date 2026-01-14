import google.generativeai as genai

genai.configure(api_key="AIzaSyCPbp-LHLid1EVhuZBRh1pZPWJk2LBzeKA")

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)
