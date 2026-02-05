"""
 VectoStores
 Uma das maneiras mais comuns de armazenar e buscar dados não estruturados é realizando o embedding e 
 armazenando os vetores resultantes e, em seguida, na hora da consulta, realizar o embedding da consulta e
 recuperar os vetores 'mais semelhantes'. Uma VectorStore faz o armazenamento dos vetores e a realização
 da busca de vetores para você.
"""

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

"""
Código para o Linux
!pip install pysqlite3-binary

__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
"""

load_dotenv()

embeddings_model = OpenAIEmbeddings(model='text-embedding-ada-002')

caminho = './arquivos/Explorando o Universo das IAs com Hugging Face.pdf'
loader = PyPDFLoader(caminho)
paginas = loader.load()

print(len(paginas))

recur_split = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50, # 10% do chunk_size
    separators=["\n\n", "\n", ".", " ", ""]
)

documentos = recur_split.split_documents(paginas)
print(len(documentos))

# Persistindo os documentos na base de dados
diretorio = "./arquivos/chroma_vectorstore"

vectorstore = Chroma.from_documents(
    documents=documentos,
    embedding=embeddings_model,
    persist_directory=diretorio
)
print(vectorstore._collection.count())

pergunta = "O que é o Hugging Face?"
docs = vectorstore.similarity_search(pergunta, k=5)
for doc in docs:
    print(doc.page_content)
    print(f"==========={doc.metadata}\n\n")

print("==" * 50)
print("Carregando BD CHROMA")
print("\n")

## Importando o vectorstore do disco
vectorstore = Chroma(
    embedding_function=embeddings_model,
    persist_directory=diretorio
)

pergunta = "O que é o Hugging Face?"
docs = vectorstore.similarity_search(pergunta, k=5)
for doc in docs:
    print(doc.page_content)
    print(f"==========={doc.metadata}\n\n")