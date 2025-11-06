import os
from dotenv import load_dotenv
from langchain_openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI()

"""
pergunta = "Conte uma breve história sobre a jornada de aprender a programar"
# print(llm.invoke(pergunta))
for trecho in llm.stream(pergunta):
    print(trecho, end="")
"""

perguntas = [
    "o que é o céu",
    "o que é a terra?",
    "o que são as estrelas?"
]

print(llm.batch(perguntas))