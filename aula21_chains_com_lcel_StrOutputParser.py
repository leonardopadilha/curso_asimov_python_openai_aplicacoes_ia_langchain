from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI()

prompt = ChatPromptTemplate.from_template('Crie uma frase sobre o seguinte assunto: {assunto}')

output_parser = StrOutputParser()

chain = prompt | model | output_parser # Dessa forma será exibido apenas a frase de retorno do modelo
print(chain.invoke({'assunto': 'futebol'}))

f"""
Atenção! A ordem importa
1. Formatar o prompt template
2. Enviar o prompt formatado para o modelo
3. Fazer o parseamento do saída do modelo

Descrição separada dos passos acima:
input = { 'assunto': 'futebol' }
prompt_formatado = prompt.invoke(input)
resposta = model.invoke(prompt_formatado)
resposta_parseada = output_parser.invoke(resposta)
"""