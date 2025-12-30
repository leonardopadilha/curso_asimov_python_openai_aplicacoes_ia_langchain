from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

prompt_curiosidade = ChatPromptTemplate.from_template('Fale uma curiosidade sobre o assunto: {assunto}')
chain_curiosidade = prompt_curiosidade | ChatOpenAI() | StrOutputParser()

prompt_historia = ChatPromptTemplate.from_template('Crie uma história sobre o seguinte fato curioso: {assunto}')
chain_historia = prompt_historia | ChatOpenAI() | StrOutputParser()

chain = chain_curiosidade | chain_historia
resposta = chain.invoke({'assunto': 'futebol'})
print(resposta)