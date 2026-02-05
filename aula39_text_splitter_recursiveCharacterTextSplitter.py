import string
from langchain_text_splitters import RecursiveCharacterTextSplitter

chunk_size = 50 # tamanho do chunk
chunk_overlap = 10 # quantos % caracteres anteriores do chunk anterior serão incluídos no chunk seguinte

char_split = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap,
    separators=['.', ' ', '']
)

texto = ''.join(f'{string.ascii_lowercase}' for _ in range(5))
#print(texto)
#print(len(texto))

novo_texto = char_split.split_text(texto)
print(novo_texto)