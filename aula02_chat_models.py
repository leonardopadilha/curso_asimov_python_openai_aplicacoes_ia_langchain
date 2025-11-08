import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

chat = ChatOpenAI(model='gpt-3.5-turbo-0125')

mensagens = [
    SystemMessage(content="Você é um assistente que conta piadas."),
    HumanMessage(content="Quanto é 1 + 1?")
]
# resposta = chat.invoke(mensagens)
# print(resposta.content)

for trecho in chat.stream(mensagens):
    print(trecho.content, end="")

