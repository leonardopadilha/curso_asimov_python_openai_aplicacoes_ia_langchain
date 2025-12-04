from dotenv import load_dotenv
from langchain_openai.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

chat_template = ChatPromptTemplate.from_messages(
    [
        ('system', 'Você é um assistente engraçado e se chama {nome_assistente}'),
        ('human', 'Olá, como vai?'),
        ('ai', 'Melhor agora! como posso ajudá-lo?'),
        ('human', '{pergunta}'),
    ]
)

chat = chat_template.format_messages(nome_assistente='Asimo', pergunta='Qual o seu nome?')
print(llm.invoke(chat).content)
