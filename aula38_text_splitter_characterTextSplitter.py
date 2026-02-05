import string
from langchain_text_splitters import CharacterTextSplitter

chunk_size = 50 # tamanho do chunk
chunk_overlap = 10 # quantos % caracteres anteriores do chunk anterior serão incluídos no chunk seguinte

char_split = CharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap,
    separator='' # separador de chunks e dessa forma, pode separar em chunks de 50 caracteres
)

texto = ''.join(f'{string.ascii_lowercase}' for _ in range(5))
#print(texto)
#print(len(texto))

splits = char_split.split_text(texto)
#print(len(splits))
#print(splits)
#print(splits[0][-10:]) # últimos 10 caracteres do primeiro chunk
#print(splits[1][:10]) # primeiros 10 caracteres do segundo chunk

texto = '''
Já conhece a lista em Python? Quer entender como manipular listas e quais são suas principais utilidades e métodos? Sabe qual a diferença entre listas e tuplas? Este artigo responde responde isso e muito mais! Aproveite ao máximo todo o potencial dessa estrutura de dados essencial para a programação em Python.

A lista em Python é uma das estruturas de dados fundamentais da linguagem Python. Além de possuir grande versatilidade, as listas são extremamente relevantes para iniciantes na programação, por incorporar uma variedade de conceitos básicos de Python como mutabilidade, indexação, iteração e slicing. Mas você já conhece as listas de Python a fundo?

Neste artigo, vamos nos aprofundar nas listas em Python e aprender a utilizá-las em seus códigos. Ao longo do texto, você aprenderá como criar e manipular uma lista em Python, quais os principais métodos de listas, e como elas se relacionam e com outros tipos de dados de Python, como strings, tuplas e vetores. Vamos lá!

'''

splits = char_split.split_text(texto)
print(splits)
