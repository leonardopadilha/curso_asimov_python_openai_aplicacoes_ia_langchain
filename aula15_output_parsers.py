from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_core import output_parsers
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

chat = ChatOpenAI(model="gpt-4o-mini")

chat_template = ChatPromptTemplate.from_messages(
    [
        ('system', 'Voçe é um assistente engraçado e se chama {nome_assistente}'),
        ('human', '{pergunta}')
    ]
)

#resposta = chat_template.format_messages(nome_assistente='Asimo', pergunta='Qual o seu nome?')
#print(resposta)
#print(resposta[0].content)

prompt = chat_template.invoke({'nome_assistente': 'Asimo', 'pergunta': 'Qual o seu nome?'})
#print(resposta)

resposta = chat.invoke(prompt)
#print(resposta)
#print(resposta.content)
output_parsers = StrOutputParser()
print(output_parsers.invoke(resposta))