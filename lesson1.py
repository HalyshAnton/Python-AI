import dotenv
import os

from langchain_huggingface import HuggingFaceEndpoint


dotenv.load_dotenv()

# res = os.getenv('HUGGINGFACEHUB_API_TOKEN')
# print(res)

llm = HuggingFaceEndpoint(
    repo_id = 'mistralai/Mistral-7B-Instruct-v0.3',
    top_k = 3,  # вибрати серед 3-ох найймовірніших слів
    top_p = 0.6, # вибрати серед слів, сума ймовірностей яких дорівнює 60%
    temperature = 0.7,
    max_new_tokens = 50 # максимальна довжина відповіді
)

# низька температура <0.3 -- мала креативність, формальні але чіткі відповіді
# висока температура >0.6 -- креативність, більш живі відповіді, але менш надійні(чіткі)
# велика температура >1.2 -- галюцинації

response = llm.invoke('Що таке Python?')
print(response)

# інструкції в mistral
response = llm.invoke('[INST]Що таке Python?[/INST]')
print(response)


# User input:   Що таке штучний інтелект?
# Model output: Штучний інтелект це набір алгоритмів які
# Results

# працюють - 30%
# обробляють - 20%
# застосовуються - 20%
# томат - 0,00000000001%

