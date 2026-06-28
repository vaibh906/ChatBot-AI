import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

chat = model.start_chat(history=[])


def get_response(message):
    try:
        response = chat.send_message(message)
        return response.text

    except Exception:
        return "Sorry, something went wrong."