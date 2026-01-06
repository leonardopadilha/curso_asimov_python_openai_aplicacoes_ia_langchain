from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

# RunnableParallel é um Runnable que executa múltiplas etapas em paralelo
# serve para executar várias etapas ao mesmo tempo usando a mesma entrada e retornar todas as saídas juntas.

load_dotenv()

model = ChatOpenAI()
prompt_nome = ChatPromptTemplate.from_template('Crie um nome para o seguinte produto: {produto}')
chain_nome = prompt_nome | model | StrOutputParser()

prompt_clientes = ChatPromptTemplate.from_template('Descreva o cliente potencial para o seguinte produto: {produto}')
chain_clientes = prompt_clientes | model | StrOutputParser()

prompt_anuncio = ChatPromptTemplate.from_template("""
Dado o produto com o seguinte nome e seguinte público potencial, desenvolva um anúncio para o produto.

# Formato de saída:
- Nome do produto: {nome_produto}
- Público: {publico}
""")

parallel = RunnableParallel({'nome_produto': chain_nome, 'publico': chain_clientes})
# resposta = parallel.invoke({'produto': 'Um copo inquebrável'})
# print(resposta)

chain = parallel | prompt_anuncio | model | StrOutputParser()
resposta = chain.invoke({'produto': 'Um copo inquebrável'})
print(resposta)