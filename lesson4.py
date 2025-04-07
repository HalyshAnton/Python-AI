import os
import dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage,
    trim_messages
)



dotenv.load_dotenv()

llm = ChatGoogleGenerativeAI(
    model='gemini-2.0-flash',
    google_api_key=os.getenv('GEMINI_API_KEY'),
)

# response = llm.invoke('привіт')
#
# print(type(response))
# print(response)

# print(os.getenv('GEMINI_API_KEY'))

# історія спілкування
messages = [
    # набір інструкцій
    SystemMessage(content='Ти ввічливіий чат бот. '
                          'Давай короткі та чіткі відповіді'),

    # історія спілкування з користувачем
    HumanMessage(content='Привіт, я Антон'),
    AIMessage(content='Привіт! Чим можу допомогти?'),
    HumanMessage(content='Яка столиця Франції'),
    AIMessage(content='Столиця Франції - Париж.'),
    HumanMessage(content='як мене звати?')
]

# response = llm.invoke(messages)
#
# print(response)

# простий чат бот

messages = [
    SystemMessage(content='Ти чат бот, який дає відповіді на питання.'
                          'Давай короткі відповіді і додатково якийсь цікавий факт')
]

# інший формат messqges
# messages = [
#     {'role': 'system',
#      'content': 'textghgkhg'},
#
#     {'role': 'human',
#      'content': 'textghgkhg'},
# ]

# while True:
#     user_input = input("Ви: ")
#
#     # зупинка розмови
#     if user_input == '':
#         break
#
#     # створити human message
#     human_message = HumanMessage(content=user_input)
#
#     # добавляємо до історії
#     messages.append(human_message)
#
#     # застосовуємо llm
#     response = llm.invoke(messages)
#
#     # добавляємо до історії
#     messages.append(response)
#
#     # print
#     print(f'AI: {response.content}')
#
#     print(messages)



# видалення зайвих повідомлень

trimmer = trim_messages(
    strategy='last', # залишати останні повідомлення
    token_counter=len, # рахуємо кількість повідомлень
    max_tokens=5, # залишати максимум 5 повідомлення
    start_on='human', # історія завжди починатиметься з HumanMessage
    end_on='human', # історія завжди закінчуватиметься з HumanMessage
    include_system=True # SystemMessage не чіпати
)

while True:
    user_input = input("Ви: ")

    # зупинка розмови
    if user_input == '':
        break

    # створити human message
    human_message = HumanMessage(content=user_input)

    # добавляємо до історії
    messages.append(human_message)

    # видалити лишнє з історії
    messages = trimmer.invoke(messages)

    # застосовуємо llm
    response = llm.invoke(messages)

    # добавляємо до історії
    messages.append(response)

    # print
    print(f'AI: {response.content}')

    # прінти
    print('messages')
    for mes in messages:
        print(repr(mes))


# об'єднати llm trimmer

chain = trimmer | llm

while True:
    user_input = input("Ви: ")

    # зупинка розмови
    if user_input == '':
        break

    # створити human message
    human_message = HumanMessage(content=user_input)

    # добавляємо до історії
    messages.append(human_message)

    # застосовуємо llm
    response = chain.invoke(messages)

    # добавляємо до історії
    messages.append(response)

    # print
    print(f'AI: {response.content}')

    # прінти
    print('messages')
    for mes in messages:
        print(repr(mes))