import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

PROMPT = """
You are a legal contract analysis assistant.

Extract the following from the contract:

1. Termination clause
2. Confidentiality clause
3. Liability clause

Also generate a summary between 100 and 150 words.

Return ONLY valid JSON in this format:

{
    "summary":"",
    "termination_clause":"",
    "confidentiality_clause":"",
    "liability_clause":""
}

Contract:

{text}
"""

def get_llm():
    return model

def analyze_contract(text):
    response = model.generate_content(PROMPT.format(text=text))

    try:
        return json.loads(response.text)
    except Exception:
        return {
            "summary": response.text,
            "termination_clause": "",
            "confidentiality_clause": "",
            "liability_clause": ""
        }