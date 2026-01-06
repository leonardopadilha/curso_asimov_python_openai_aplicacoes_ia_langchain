from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatOpenAI()
prompt = ChatPromptTemplate.from_template('Crie uma frase sobre o assunto: {assunto}')

chain = prompt | model
"""
# invoke é o método básico para inserir uma input na cadeia e receber uma resposta
resposta = chain.invoke({'assunto': 'futebol'})
print(resposta.content)
"""

"""
# stream é o método para receber uma saída conforme ela é gerada pelo modelo
resposta = chain.stream({'assunto': 'futebol'})
for trecho in resposta:
    print(trecho.content, end="")
"""

# batch é o método para fazer múltiplas requisições em paralelo
respostas = chain.batch([{'assunto': 'futebol'}, {'assunto': 'volei'}, {'assunto': 'basquete'}])
for resposta in respostas:
    print(resposta.content)

# Limitar quantas execuções deseja ao mesmo tempo: 
# respostas = chain.batch([{'assunto': 'futebol'}, {'assunto': 'volei'}, {'assunto': 'basquete'}], config={'max_concurrency': 2})