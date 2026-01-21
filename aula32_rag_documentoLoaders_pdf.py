from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain.chains.question_answering import load_qa_chain
from langchain_openai.chat_models import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI(model='gpt-3.5-turbo-0125')

caminho = './arquivos/Explorando o Universo das IAs com Hugging Face.pdf'
loader = PyPDFLoader(caminho)
documentos = loader.load()

#print(len(documentos))
#print(documentos[3].page_content)
#print(documentos[3].metadata)

chain = load_qa_chain(llm=chat, chain_type='stuff', verbose=True)

pergunta = 'Quais assuntos são tratados no documento?'

resposta = chain.run(input_documents=documentos[:10], question=pergunta)
print(resposta)