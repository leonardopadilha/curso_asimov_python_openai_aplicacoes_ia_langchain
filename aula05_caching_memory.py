import time
from dotenv import load_dotenv
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.caches import InMemoryCache
from langchain_core.globals import set_llm_cache

set_llm_cache(InMemoryCache())  # volátil (só dura enquanto o processo roda)
load_dotenv()

chat = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)

mensagens = [
    SystemMessage(content="Você é um assistente engraçado."),
    HumanMessage(content="Quanto é 1 + 1?"),
]

#t0 = time.time()
#r1 = chat.invoke(mensagens)
#t1 = time.time()

# Segunda chamada idêntica (deve ser instantânea se cacheou)
r2 = chat.invoke(mensagens) # O método invoke é o responsável por enviar a mensagem para o modelo
t2 = time.time()

#print("1ª resposta:", r1.content, f"(demorou {t1 - t0:.3f}s)")
#print("2ª resposta:", r2.content, f"(demorou {t2 - t1:.3f}s)  <- cache hit")
print(r2.content)

"""
AIMessage -> Representa uma mensagem gerada pelo modelo
HumanMessage -> Representa uma mensagem enviada pelo usuário
SystemMessage -> Indica ao modelo como se comportar
"""