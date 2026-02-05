from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.chroma import Chroma
from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai.chat_models import ChatOpenAI
from langchain.chains.retrieval_qa.base import RetrievalQA

load_dotenv()

caminhos = [
    "./arquivos/Explorando o Universo das IAs com Hugging Face.pdf",
    "./arquivos/Explorando a API da OpenAI.pdf"
]

paginas = []
for caminho in caminhos:
    loader = PyPDFLoader(caminho)
    paginas.extend(loader.load())

recur_split = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100,
    separators=["\n\n", "\n", ".", " ", ""]
)

documents = recur_split.split_documents(paginas)

for i, doc in enumerate(documents):
    doc.metadata['source'] = doc.metadata['source'].replace('./arquivos/', '')
    doc.metadata['doc_id'] = i

diretorio = "./arquivos/chroma_retrival_bd"

embeddings_model = OpenAIEmbeddings()
vectordb = Chroma.from_documents(
    documents=documents,
    embedding=embeddings_model,
    persist_directory=diretorio
)

chat = ChatOpenAI(model='gpt-3.5-turbo-0125')

chat_chain = RetrievalQA.from_chain_type(
    llm=chat,
    retriever=vectordb.as_retriever(search_type='mmr')
)

pergunta = 'O que é Hugging Face e como faço para acessá-lo?'
resposta = chat_chain.invoke({'query': pergunta})
print(resposta['result'])