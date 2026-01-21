from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain.chains.question_answering import load_qa_chain
from langchain_openai.chat_models import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

caminho = './arquivos/Top 1000 IMDB movies.csv'

loader = CSVLoader(caminho)
documentos = loader.load()
print(documentos[0].page_content)
print(documentos[0].metadata)

chat = ChatOpenAI(model='gpt-3.5-turbo-0125')

chain = load_qa_chain(llm=chat, chain_type='stuff', verbose=True)

pergunta = 'Qual é o filme com maior metascore?'
resposta = chain.run(input_documents=documentos[:10], question=pergunta)
print(resposta)