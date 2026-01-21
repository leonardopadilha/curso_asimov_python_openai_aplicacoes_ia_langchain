"""
Memory
A maioria das aplicações de Modelos de LLM possui uma interface conversacional. Um componente 
essencial de uma conversa é a capacidade de se referir a informações introduzidas anteriormente 
na conversa. No mínimo, um sistema conversacional deve ser capaz de acessar diretamente alguma 
janela de mensagens passadas. Um sistema mais complexo precisará ter um modelo de mundo que 
está constantemente atualizando, o que lhe permite fazer coisas como manter informações sobre 
entidades e suas relações.

Chamamos essa capacidade de armazenar informações sobre interações passadas de "Memory", ou 
memória. LangChain oferece muitas utilidades para adicionar memória a um sistema. Essas utilidades 
podem ser usadas por si só ou incorporadas de maneira integrada em uma chain.
"""

from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai.chat_models import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

memory = InMemoryChatMessageHistory()

#memory.add_user_message("Olá, modelo!")
#memory.add_ai_message("Olá, user!")

#print(memory.messages)

prompt = ChatPromptTemplate.from_messages([
    ("system", "Você é um tutor de programação chamado Asimo. Responda as perguntas de forma didática."),
    ("placeholder", "{memoria}"),
    ("human", "{pergunta}")
])

chain = prompt | ChatOpenAI()

store = {}
def get_by_session_id(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

chain_com_memoria = RunnableWithMessageHistory(
    chain,
    get_by_session_id,
    input_messages_key='pergunta',
    history_messages_key='memoria'
)

config = {'configurable': {'session_id': 'usuaria_a'}}
resposta = chain_com_memoria.invoke({'pergunta': 'O meu nome é Leo'}, config=config)
print(resposta.content)

resposta = chain_com_memoria.invoke({'pergunta': 'Qual é o meu nome?'}, config=config)
print(resposta.content)

config = {'configurable': {'session_id': 'usuaria_b'}}
resposta = chain_com_memoria.invoke({'pergunta': 'Qual é o meu nome?'}, config=config)
print(resposta.content)