import requests
import os
from dotenv import load_dotenv
load_dotenv()

RAPID_API_KEY = os.getenv("RAPID_API_KEY")
RAPID_API_HOST = "rapid-translate-multi-traduction.p.rapidapi.com"

def translate_text(spanish_text):
    url = f"https://{RAPID_API_HOST}/t"

    headers = {
        "Content-Type": "application/json",
        "x-rapidapi-host": RAPID_API_HOST,
        "x-rapidapi-key": RAPID_API_KEY
    }

    payload = {
        "from": "es",
        "to": "en",
        "q": spanish_text
    }
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        response.raise_for_status()
        translated_list = response.json() 
        return translated_list[0] if translated_list else "Translation failed"

    except Exception as e:
        return f"Translation failed: {str(e)}"
