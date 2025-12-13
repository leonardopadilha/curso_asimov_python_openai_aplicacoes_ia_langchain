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

output_parsers = StrOutputParser()

chain = chat_template | chat | output_parsers
print(chain.invoke({'nome_assistente': 'Asimo', 'pergunta': 'Qual o seu nome?'}))