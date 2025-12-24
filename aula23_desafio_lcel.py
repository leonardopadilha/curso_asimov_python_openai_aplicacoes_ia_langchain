from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

texto = input("Please type some text in English: ")

llm = ChatOpenAI(model="gpt-3.5-turbo")

prompt = ChatPromptTemplate.from_template('Por favor, traduza o seguinte texto para o português: {texto}')

output_parser = StrOutputParser()

chain = prompt | llm | output_parser
resposta = chain.invoke({'texto': texto})
print(resposta)