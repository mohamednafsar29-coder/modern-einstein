# modern-einstein
🧠 Professor Einstein's Laboratory 🧪

An interactive AI-powered scientific assistant built with Streamlit and Ollama, where Albert Einstein is reborn in the modern era to explain science with depth, clarity, and imagination.

“Imagination is more important than knowledge.” – Albert Einstein

📌 Overview

Professor Einstein's Laboratory is a themed conversational AI application that simulates Albert Einstein’s teaching style.

The assistant:

Explains complex scientific concepts simply and deeply

Uses analogies and step-by-step reasoning

Encourages curiosity and critical thinking

Maintains a calm, professor-like tone

The application is powered by:

Streamlit for the interactive web interface

Ollama for local LLM inference

A structured system prompt to maintain Einstein’s personality

🚀 Features

🧠 Einstein-inspired AI personality

🎨 Custom scientific dark theme UI

⚙️ Adjustable creativity (temperature slider)

🧹 Clear conversation functionality

💬 Persistent session-based chat history

🔬 Structured and educational responses

🛠️ Tech Stack
Technology	Purpose
Streamlit	Frontend UI
Ollama	Local LLM inference
Python	Backend logic
📦 Installation
1️⃣ Clone the Repository
git clone https://github.com/your-username/einstein-laboratory.git
cd einstein-laboratory
2️⃣ Install Dependencies
pip install streamlit ollama
3️⃣ Install and Run Ollama

Download and install Ollama from:

👉 https://ollama.com

Pull the required model:

ollama pull gemma3
▶️ Running the Application
streamlit run app.py

The application will open in your browser at:

http://localhost:8501
🎛️ Configuration

Inside the sidebar:

Model Selector – Choose the available Ollama model

Temperature Slider – Adjust creativity (0.0–1.5)

Clear Conversation – Reset session chat

🧠 System Personality

The assistant:

Always remains in character as Albert Einstein

Provides structured and detailed explanations

Defines technical terms clearly

Redirects non-scientific questions toward scientific reasoning

📂 Project Structure
einstein-laboratory/
│
├── app.py              # Main Streamlit application
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies (optional)
🔮 Future Improvements

Multi-model support

Scientific topic selection

Chat export feature

Voice interaction

Deployment version (Cloud / Docker)

📜 License

This project is for educational and experimental purposes.

You may modify and use it freely.

👨‍🔬 Author

Developed by mohamed nafsar D
