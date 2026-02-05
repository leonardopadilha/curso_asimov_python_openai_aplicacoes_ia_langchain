from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.chroma import Chroma
from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai.llms import OpenAI
from langchain.retrievers.self_query.base import SelfQueryRetriever
from langchain.chains.query_constructor.schema import AttributeInfo
from langchain.globals import set_debug

set_debug(False)

load_dotenv()

embeddings_model = OpenAIEmbeddings()

metadata_info = [
    AttributeInfo(
        name='source',
        description='Nome da apostila de onde o texto original foi retirado. Deve ter o valor de: \
            Explorando o Universo das IAs com Hugging Face.pdf ou Explorando a API da OpenAI.pdf',
        type='string'
    ),
    AttributeInfo(
        name='page',
        description='A página da apostila de onde o texto se origina',
        type='integer'
    )
]

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

#print(documents[2].metadata)

diretorio = "./arquivos/chroma_retrival_bd"

vectordb = Chroma.from_documents(
    documents=documents,
    embedding=embeddings_model,
    persist_directory=diretorio
)

document_description = 'Apostilas de cursos'
llm = OpenAI()
retriever = SelfQueryRetriever.from_llm(
    llm,
    vectordb,
    document_description,
    metadata_info,
    verbose=False
)

pergunta = "Quais detalhes são descritos na página 44 da apostila Explorando a API da OpenAI?"

docs = retriever.invoke(pergunta)
for doc in docs:
    print(doc.page_content)
    print(f"==========={doc.metadata}\n\n")






