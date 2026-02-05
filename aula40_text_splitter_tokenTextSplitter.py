import string
from langchain_text_splitters import TokenTextSplitter

chunk_size = 50 # tamanho dos tokens do chunk
chunk_overlap = 5 # quantos % caracteres anteriores do chunk anterior serão incluídos no chunk seguinte

char_split = TokenTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap
)

texto = ''.join(f'{string.ascii_lowercase}' for _ in range(5))
#print(texto)
#print(len(texto))

novo_texto = char_split.split_text(texto)
print(novo_texto)