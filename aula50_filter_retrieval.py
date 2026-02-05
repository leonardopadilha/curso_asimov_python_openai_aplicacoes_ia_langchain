from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.chroma import Chroma
from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

embeddings_model = OpenAIEmbeddings()

"""
Código para o Linux
!pip install pysqlite3-binary

__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
"""

caminhos = [
    "./arquivos/Explorando o Universo das IAs com Hugging Face.pdf",
    "./arquivos/Explorando a API da OpenAI.pdf",
    "./arquivos/Explorando a API da OpenAI.pdf",
]

paginas = []

for caminho in caminhos:
    loader = PyPDFLoader(caminho)
    paginas.extend(loader.load())

recur_split = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    separators=["\n\n", "\n", ".", " ", ""]
)

documents = recur_split.split_documents(paginas)

for i, doc in enumerate(documents):
    doc.metadata['source'] = doc.metadata['source'].replace('./arquivos/', '')
    doc.metadata['doc_id'] = i

#print(documents[2].metadata)

diretorio = "./arquivos/chroma_retrival_bd"

vectordb = Chroma.from_documents(
    documents=documents,
    embedding=embeddings_model,
    persist_directory=diretorio
)

# MMR => Maximal Marginal Relevance
pergunta = "O que a apostila de Hugging Face fala sobre a OpenAI e o ChatGPT?"
docs = vectordb.similarity_search(pergunta, k=3, filter={'source': 'Explorando o Universo das IAs com Hugging Face.pdf'})
for doc in docs:
    print(doc.page_content)
    print(f"==========={doc.metadata}\n\n")

