from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatOpenAI()

prompt = ChatPromptTemplate.from_template('Crie uma frase sobre o seguinte assunto: {assunto}')

chain = prompt | model
print(chain.invoke({'assunto': 'futebol'}))