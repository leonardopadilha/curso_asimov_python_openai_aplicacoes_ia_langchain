from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

prompt = ChatPromptTemplate.from_template("""
Você é um professor de matemática de ensino fundamental capaz de dar respostas muito detalhadas e
didáticas. Responda a seguinte pergunta de um aluno: Pergunta: {pergunta}""")
chain_matematica = prompt | model

prompt = ChatPromptTemplate.from_template("""
Você é um professor de física de ensino fundamental capaz de dar respostas muito detalhadas e 
didáticas. Responda a seguinte pergunta de um aluno: Pergunta: {pergunta}""")
chain_fisica = prompt | model

prompt = ChatPromptTemplate.from_template("""
Você é um professor de história de ensino fundamental capaz de dar respostas muito detalhadas e
didáticas. Responda a seguinte pergunta de um aluno: Pergunta: {pergunta}""")
chain_historia = prompt | model

prompt = ChatPromptTemplate.from_template("""{pergunta}""")
chain_generica = prompt | model


prompt = ChatPromptTemplate.from_template("""
Você deve categorizar a seguinte pergunta: {pergunta}""")

class Categorizador(BaseModel):
    """ Categoriza as perguntas de alunos do ensino fundamental """
    area_conhecimento: str = Field(description='A área de conhecimento da pergunta feita pelo \
    aluno. Deve ser "matemática", "física" ou "história". Caso não se encaixe em nenhuma delas, \
    retorne "outra"')

model_estruturado = prompt | model.with_structured_output(Categorizador)
# print(model_estruturado.invoke({'pergunta': 'O que é o homem?'}))


# chain = RunnablePassthrough().assign(categoria=model_estruturado)
#print(chain.invoke({'pergunta': 'Quando foi a independência dos estados unidos?'}))

def route(input):
    if input['categoria'].area_conhecimento == 'matemática':
        return chain_matematica
    if input['categoria'].area_conhecimento == 'física':
        return chain_fisica
    if input['categoria'].area_conhecimento == 'história':
        return chain_historia
    return chain_generica


pergunta = {
    'historia': 'Quando foi a independência dos estados unidos?',
}

chain = RunnablePassthrough().assign(categoria=model_estruturado) | route
resposta = chain.invoke({'pergunta': pergunta['historia']})
print(resposta.content)

print("*" * 100)
chain = RunnablePassthrough().assign(categoria=model_estruturado)
print(chain.invoke({'pergunta': pergunta['historia']}))