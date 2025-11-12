import os
from dotenv import load_dotenv
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_community.cache import SQLiteCache
from langchain.globals import set_llm_cache

set_llm_cache(SQLiteCache(database_path='arquivos/lancgchain_cache_db.sqlite'))

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

chat = ChatOpenAI(model='gpt-3.5-turbo-0125')

mensagens = [
    SystemMessage(content='Você é um assistente engraçado.'),
    HumanMessage(content= 'Quanto é 1 + 1?'),
]


resposta = chat.invoke(mensagens)
print(resposta.content)