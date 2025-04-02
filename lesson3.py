import dotenv
import warnings

from langchain_huggingface import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema


warnings.filterwarnings('ignore') # ігнорувати warnings
dotenv.load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = 'mistralai/Mistral-7B-Instruct-v0.3',
    temperature = 0.2,
)


# response = llm.invoke('Коли була висадка на Місяць?')
# print(response)

# prompt template
prompt = PromptTemplate.from_template(
    """
    [INST] Ти помічник по навчанню учнів.
    Твої відповіді інформативні, стислі та цікаві.
    Відповідь має бути короткою.
    [/INST]
    
    [INST]
    Питання: {question}
    Довжина відповіді: {length}
    Відповідь:
    [/INST] 
    """
)

# question = input('Введіть питання: ')
# result = prompt.format(question=question)
#
# response = llm.invoke(result)
# print(response)

# ланцюг
# chain = prompt | llm
#
# user_question = input('Введіть питання: ')
#
# data = {'question': user_question,
#         'length': '3 реченя'
#         }
#
# response = chain.invoke(data)
# print(response)


# output parser
schemas = [
    ResponseSchema(name='answer', description='Відповідь на питання користувача'),
    ResponseSchema(name='user_input', description='Питання користувача'),
]

parser = StructuredOutputParser.from_response_schemas(schemas)
format_instructions = parser.get_format_instructions()

prompt = PromptTemplate.from_template(
    """
    [INST] Ти помічник по навчанню учнів.
    Твої відповіді інформативні, стислі та цікаві.
    Відповідь має бути короткою.
    [/INST]

    [INST]
    Питання: {question}
    Довжина відповіді: {length}
    Формат відповіді: {format_instructions}
    Відповідь:
    [/INST] 
    """,
    partial_variables={'format_instructions': format_instructions,
                       'length': '50 слів'}
)

# ланцюг
# chain = prompt | llm | parser
#
# user_question = input('Введіть питання: ')
#
# data = {'question': user_question}
#
# # result = prompt.format(question=user_question,
# #                        length='3 реченя')
#
# response = chain.invoke(data)
# print(type(response))
# print(response)
#
# key = 'answer'
# print(response[key])



# Напишіть 2 ланцюга
# Перший визначає тему питаня та дає відповідь на питання
# Другий рекомендує список цікавих фактів по темі питання


# перший ланцюг

schemas = [
    ResponseSchema(name='topic', description='Тема питання'),
    ResponseSchema(name='answer', description='відповідь на питання користувача'),
]

parser = StructuredOutputParser.from_response_schemas(schemas)
format_instructions = parser.get_format_instructions()

prompt = PromptTemplate.from_template(
    """
    [INST]Ти помічник по навчанню. Твоя задача давати відповідь на питання.
    Твої відповіді влучні, чіткі та короткі.
    Перед відповідю тобі потрібно визначити тему питання(наука, історія, тощо).
    Відповідай українською мовою.
    [/INST]
    
    [INST]
    Питання: {question}
    Формат відповіді: {format}
    
    Тема питання:
    Відповідь:
    [/INST]
    """,
    partial_variables={'format': format_instructions}
)

chain1 = prompt | llm | parser

# другий ланцюг
schemas = [
    ResponseSchema(name='recommendations', description='Список цікавих фактів по заданій темі')
]

parser = StructuredOutputParser.from_response_schemas(schemas)
format_instructions = parser.get_format_instructions()

prompt = PromptTemplate.from_template(
    """
    [INST]Ти помічник по навчанню. Твоя задача рекомендувати
    список цікавих фактів по заданій темі. 
    Назви фактів мають бути короткими.
    Кількість фактів менше 6.
    Відповідай українською мовою
    [/INST]
    
    [INST]
    Тема: {topic}
    Формат відповіді: {format}
    Відповідь: 
    [/INST]
    """,
    partial_variables={'format': format_instructions}
)

chain2 = prompt | llm | parser


# остаточна модель

user_question = input('Введіть питання: ')

data = {'question': user_question}

response1 = chain1.invoke(data)
response2 = chain2.invoke(response1)

print(response1)
print(response2)

fact = response2['recommendations'][2]
print(fact)
