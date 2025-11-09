import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
#import langchain

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

chat = ChatOpenAI()

prompt = "Resposta apenas com o resultado da operação: "

mensagens = [
    HumanMessage(content= f'{prompt} Quanto é 1 + 1?'),
    AIMessage(content='2'),
    HumanMessage(content= f'{prompt} Quanto é 10 * 5?'),
    AIMessage(content='50'),
    HumanMessage(content= f'{prompt} Quanto é 10 + 3?'),
]

#langchain.debug = True
resposta = chat.invoke(mensagens)
print(resposta.content)