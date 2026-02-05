"""
Código para o Linux
!pip install pysqlite3-binary

__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
"""

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.faiss import FAISS
from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_openai.chat_models import ChatOpenAI

load_dotenv()

caminhos = [
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

vectorstore = FAISS.from_documents(
    documents=documents,
    embedding=OpenAIEmbeddings()
)

prompt = ChatPromptTemplate.from_template(
    """ Responda as perguntas se baseando no contexto fornecido.
    contexto: {contexto}
    pergunta: {pergunta}
    """
)

def join_documents(input):
    input['contexto'] = '\n\n'.join([c.page_content for c in input['contexto']])
    return input

retriever = vectorstore.as_retriever(search_type='mmr', search_kwargs={'k': 5, 'fetch_k': 25})

setup = RunnableParallel({
    'pergunta': RunnablePassthrough(),
    'contexto': retriever
}) | join_documents

input = setup.invoke('O que é a OpenAI?')
#print(input)
#print(input['contexto'])

chain = setup | prompt | ChatOpenAI()
resposta = chain.invoke('O que é a OpenAI?')
print(resposta.content)