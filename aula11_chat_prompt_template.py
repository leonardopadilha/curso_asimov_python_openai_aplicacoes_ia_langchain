#from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate

#load_dotenv()

chat_template = ChatPromptTemplate.from_template('Essa é a minha dúvida: {duvida}')
chat = chat_template.format_messages(duvida='Quem sou eu?')
print(chat)
