import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Get API Key
API_KEY = os.getenv("GEMINI_API_KEY")

# Check if API key exists
if not API_KEY:
    print("❌ Error: GEMINI_API_KEY not found in .env file")
    exit()

# Configure Gemini
genai.configure(api_key=API_KEY)

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

# Start chat with memory
chat = model.start_chat(history=[])

print("=" * 50)
print("🤖 Gemini AI Chatbot")
print("Type 'exit' to quit")
print("=" * 50)

while True:
    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("\n👋 Goodbye!")
        break

    try:
        response = chat.send_message(user_input)

        print("\n🤖 Bot:")
        print(response.text)

    except Exception as e:
        print("\n❌ Error:", e)