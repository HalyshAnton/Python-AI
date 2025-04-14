import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage,
    trim_messages
)

llm = ChatGoogleGenerativeAI(
    model='gemini-2.0-flash',
    google_api_key=st.secrets.get('GEMINI_API_KEY'),
)

# головний заголовок
st.title('ITStep чат-бот')

# простий текст
st.markdown('простий чат бот для спілкування. Модель gemini-2.0-flash')

# st.markdown(user_input)
#
# print(user_input)

# додаємо історію повідомлень до сесії

# якщо це тільки початок застосутку, додаємо історію повідомлень
if 'messages' not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="""
        Ти ввічливий чат бот. Відповідай коротко та чітко
        """)
    ]

# місце для вводу повідомлення від користувача
user_input = st.chat_input('Введіть ваше повідомлення ')

# якщо користувач щось ввів
if user_input is not None:
    # додати повідомлення від користувача в історію
    human_message = HumanMessage(content=user_input)
    st.session_state.messages.append(human_message)

    # виклик моделі
    response = llm.invoke(st.session_state.messages)

    # додати відповідь моделі до історії
    st.session_state.messages.append(response)


# відображення історії спілкування(в streamlit)

for message in st.session_state.messages:
    # перевіряємо хто писав повідомлення
    if isinstance(message, HumanMessage): # перевірка на тип даних
        role = 'human'
    elif isinstance(message, AIMessage): # перевірка на тип даних
        role = 'ai'
    else: # system message пропускаємо
        continue

    with st.chat_message(role):
        st.markdown(message.content)