from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

chunk_size = 250
chunk_overlap = 25

char_split = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap,
)

caminho = './arquivos/Explorando o Universo das IAs com Hugging Face.pdf'
loader = PyPDFLoader(caminho)
docs = loader.load()

print(len(docs))

# split_documents: divide os documentos em chunks
# split_text: divide o texto em chunks

splits = char_split.split_documents(docs)
print(len(splits))
#print(splits)