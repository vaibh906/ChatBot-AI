# 🤖 Gemini AI Chatbot

A modern AI-powered chatbot built with **Python**, **Flask**, **HTML**, **CSS**, and **JavaScript**, integrated with **Google Gemini AI**.

This project provides a clean web interface where users can chat with Google's Gemini model in real time.

---

# 📖 About the Project

This chatbot allows users to communicate with Google's Gemini AI through a modern web interface instead of using the terminal.

The project demonstrates how to:

- Build a Flask web application
- Connect a frontend with a Python backend
- Integrate the Google Gemini API
- Manage API keys securely using `.env`
- Exchange data using JSON and Fetch API
- Build responsive user interfaces using HTML, CSS and JavaScript

This project is beginner-friendly and can also be used as a base for advanced AI applications.

---

# ✨ Features

- 🤖 AI Powered Chatbot
- 💬 Real-Time Conversation
- 🌐 Flask Web Application
- 🎨 Responsive User Interface
- 🔐 Secure API Key using `.env`
- ⚡ Fast Responses
- 🧠 Gemini 2.5 Flash Integration
- 📱 Mobile Friendly
- 💻 Clean Project Structure

---

# 🛠 Technologies Used

## Backend

- Python
- Flask

## Frontend

- HTML5
- CSS3
- JavaScript

## AI

- Google Gemini API

## Version Control

- Git
- GitHub

---

# 📂 Project Structure

```
Chatbot_AI/
│
├── app.py
├── chatbot.py
├── .env
├── .gitignore
├── requirements.txt
├── README.md
│
├── templates/
│      └── index.html
│
├── static/
│      ├── css/
│      │      └── style.css
│      │
│      ├── js/
│      │      └── script.js
│      │
│      └── images/
│
└── venv/
```

---

# ⚙️ Installation Guide

## 1 Clone Repository

```bash
git clone https://github.com/yourusername/Chatbot_AI.git
```

---

## 2 Move into Project Folder

```bash
cd Chatbot_AI
```

---

## 3 Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

---

## 4 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5 Create a .env File

Inside the project folder create

```
.env
```

Add your Gemini API Key

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

## 6 Run the Project

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

# 🧠 How It Works

```
            User
              │
              ▼
       HTML Interface
              │
              ▼
        JavaScript
              │
              ▼
       Flask Backend
              │
              ▼
       Gemini AI Model
              │
              ▼
         AI Response
              │
              ▼
        Browser Screen
```

---

# 🔄 Request Flow

```
User Message

      │

      ▼

JavaScript (Fetch API)

      │

      ▼

Flask Route (/chat)

      │

      ▼

chatbot.py

      │

      ▼

Gemini API

      │

      ▼

AI Response

      │

      ▼

Return JSON

      │

      ▼

Display on Website
```

---

# 🔒 Environment Variables

This project uses a `.env` file to keep sensitive information secure.

Example

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Never upload your `.env` file to GitHub.

---

# 📦 Required Packages

- Flask
- python-dotenv
- google-generativeai

Install all packages using

```bash
pip install -r requirements.txt
```

---

# 🚀 Future Improvements

- Chat History
- Multiple Conversations
- Dark / Light Mode
- Typing Animation
- Markdown Support
- Code Highlighting
- User Authentication
- Database Integration
- Voice Input
- Image Upload
- File Upload
- Export Chat
- Responsive Mobile Design
- Docker Support
- Deployment

---

# 🎯 Learning Objectives

This project demonstrates:

- Python Programming
- Flask Framework
- REST API Concepts
- HTML
- CSS
- JavaScript
- Fetch API
- JSON
- Environment Variables
- Git
- GitHub
- AI API Integration

---

# 🤝 Contributing

Contributions are welcome!

If you would like to improve this project:

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push your branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# 👨‍💻 Author

**Vaibhav Pande**

Artificial Intelligence & Data Science Student

GitHub:
https://github.com/YOUR_USERNAME

LinkedIn:
YOUR_LINKEDIN

---

# ⭐ Support

If you found this project helpful,

please ⭐ Star the repository.

It motivates me to build more open-source AI projects.

---

# 📜 License

This project is licensed under the MIT License.

Feel free to use, modify and improve it for learning purposes.

---

## Thank You ❤️

Happy Coding 🚀
