from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# RunnablePassthrough é um Runnable que passa as variáveis de entrada para a próxima etapa
# simplesmente repassa a entrada adiante, sem modificar nada

prompt_nome = ChatPromptTemplate.from_template('Crie um nome para o seguinte produto: {produto}')
chain_nome = prompt_nome | ChatOpenAI() | StrOutputParser()

prompt_clientes = ChatPromptTemplate.from_template('Descreva o cliente potencial para o seguinte produto: {produto}')
chain_clientes = prompt_clientes | ChatOpenAI() | StrOutputParser()

prompt_anuncio = ChatPromptTemplate.from_template("""
Dado o produto com o seguinte nome e seguinte público potencial, desenvolva um anúncio para o produto.

# Formato de saída:
- Nome do produto: {nome_produto}
- Característica do produto: {produto}
- Público: {publico}
""")

parallel = RunnablePassthrough().assign(**{'nome_produto': chain_nome, 'publico': chain_clientes})
chain = parallel | prompt_anuncio | ChatOpenAI() | StrOutputParser()
resposta = chain.invoke({'produto': 'Um copo inquebrável'})
print(resposta)