import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

# --- Initialize Gemini ---
model = ChatGoogleGenerativeAI(
    model='gemini-2.0-flash',
    google_api_key=st.secrets.get('GEMINI_API_KEY'),
)

# --- Streamlit UI ---
st.title("💬 Gemini Chatbot")
st.markdown("Ask me anything!")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --- Input form ---
user_input = st.chat_input("Введіть запит...")
if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    with st.spinner("Gemini думає..."):
        response = model.invoke(st.session_state.chat_history)
        print(response)
    st.session_state.chat_history.append({"role": "ai", "content": response.content})

# --- Chat history rendering ---
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])