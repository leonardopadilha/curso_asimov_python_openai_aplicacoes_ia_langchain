"""
 VectoStores
 Uma das maneiras mais comuns de armazenar e buscar dados não estruturados é realizando o embedding e 
 armazenando os vetores resultantes e, em seguida, na hora da consulta, realizar o embedding da consulta e
 recuperar os vetores 'mais semelhantes'. Uma VectorStore faz o armazenamento dos vetores e a realização
 da busca de vetores para você.

 https://python.langchain.com/docs/integrations/vectorstores
"""

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores.faiss import FAISS

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
diretorio = "./arquivos/faiss_bd"

## Importando o vectorstore do disco
vectorstore = FAISS.from_documents(
    documents=documentos,
    embedding=embeddings_model
)

pergunta = "O que é o Hugging Face?"
docs = vectorstore.similarity_search(pergunta, k=5)
for doc in docs:
    print(doc.page_content)
    print(f"==========={doc.metadata}\n\n")

print("==" * 50)
print("Salvando BD FAISS")
print("\n\n")

# Salvando BD FAISS
vectorstore.save_local(diretorio)

# Importando BD FAISS
vectorstore = FAISS.load_local(
    diretorio, 
    embeddings=embeddings_model,
    # Desabilita a verificação de segurança, se não conhece a base de dados é melhor não colocar essa linha
    allow_dangerous_deserialization=True
)

pergunta = "O que é o Hugging Face?"
docs = vectorstore.similarity_search(pergunta, k=5)
for doc in docs:
    print(doc.page_content)
    print(f"==========={doc.metadata}\n\n")