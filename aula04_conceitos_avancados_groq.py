import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage
from langchain_groq import ChatGroq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
MODELO='llama-3.3-70b-versatile'

chat = ChatGroq(
    api_key=api_key,
    model=MODELO,
)

prompt = "Resposta apenas com o resultado da operação: "

mensagens = [
    HumanMessage(content= f'{prompt} Quanto é 1 + 1?'),
    AIMessage(content='2'),
    HumanMessage(content= f'{prompt} Quanto é 10 * 5?'),
    AIMessage(content='50'),
    HumanMessage(content= f'{prompt} Quanto é 10 + 3?'),
]

resposta = chat.invoke(mensagens)
print(resposta.content)