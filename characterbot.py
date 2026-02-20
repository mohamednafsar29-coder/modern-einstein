import streamlit as st
import ollama

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Professor Einstein's Laboratory",
    layout="centered"
)

# -----------------------------
# Custom Scientist Theme (CSS)
# -----------------------------
st.markdown("""
<style>
/* Background */
.stApp {
    background-color: #0b132b;
    color: #eaeaea;
    font-family: 'Segoe UI', sans-serif;
}

/* Title */
h1 {
    color: #4cc9f0;
    text-align: center;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #1c2541;
    border-right: 2px solid #4cc9f0;
}

/* Chat messages */
[data-testid="stChatMessage"] {
    border: 1px solid #4cc9f0;
    border-radius: 12px;
    padding: 10px;
    margin-bottom: 10px;
    box-shadow: 0 0 8px rgba(76,201,240,0.3);
}

/* Input box */
[data-testid="stChatInput"] textarea {
    background-color: #1c2541;
    color: white;
}

/* Buttons */
.stButton > button {
    background-color: #4cc9f0;
    color: black;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Title and Quote
# -----------------------------
st.title("🧠 Professor Einstein's Laboratory 🧪")
st.markdown(
    "<p style='text-align:center; color:#a9def9;'>"
    "“Imagination is more important than knowledge.”</p>",
    unsafe_allow_html=True
)

# -----------------------------
# Sidebar Controls
# -----------------------------
with st.sidebar:
    st.header("⚙️ Control Panel")

    model = st.selectbox(
        "Choose Model",
        ["gemma3:latest"]
    )

    temperature = st.slider(
        "Creativity (Temperature)",
        0.0, 1.5, 0.7, 0.1
    )

    if st.button("🧹 Clear Conversation"):
        st.session_state.messages = []
        st.rerun()

# -----------------------------
# System Prompt (Einstein Character)
# -----------------------------
EINSTEIN_PROMPT = """
You are Albert Einstein, the legendary theoretical physicist, reborn in the modern era.

Your personality:
- Speak in a thoughtful, intelligent, and slightly philosophical tone.
- Explain scientific concepts deeply yet simply.
- Use analogies and real-world examples.
- Encourage curiosity, imagination, and critical thinking.
- Occasionally add reflective remarks about science.

Your knowledge domain includes:
Physics (Relativity, Quantum Mechanics, Thermodynamics),
Mathematics, Astronomy, Cosmology, Chemistry fundamentals,
Biology basics, modern scientific discoveries, and philosophy of science.

Response style:
- Structured and detailed explanations.
- Step-by-step reasoning when needed.
- Define technical terms clearly.
- Calm, professor-like tone.
- No casual slang.

Rules:
- Always remain in character as Albert Einstein.
- Never say you are an AI or language model.
- Speak as if explaining to a curious student.
- If a question is outside science, gently redirect it toward scientific reasoning.
"""

# -----------------------------
# Session State
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": EINSTEIN_PROMPT}
    ]

# -----------------------------
# Display Chat History
# -----------------------------
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

# -----------------------------
# Chat Input
# -----------------------------
user_input = st.chat_input("Ask a scientific question...")

if user_input:
    # User message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.write(user_input)

    # Model response
    response = ollama.chat(
        model=model,
        messages=st.session_state.messages,
        options={"temperature": temperature}
    )

    reply = response["message"]["content"]

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

    with st.chat_message("assistant"):
        st.write(reply)
