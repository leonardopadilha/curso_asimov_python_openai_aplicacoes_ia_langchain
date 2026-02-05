"""
Os Embeddings criam uma representação vetorial de um pedaço de texto. Isso é útil porque significa que podemos
pensar sobre o texto no espaço vetorial e fazer coisas como busca semântica, onde procuramos por pedaços de texto
que são ais semelhantes no espaço vetorial, ou seja, que estão a uma distância menor.

A classe Embeddings do LangChain é uma classe projetada para interagir com modelos de embeddings de texto. Existem
muitos modelos diferentes (OpenAI, Cohere, Hugging Face, etc) - esta classe é projetada para fornecer uma
interface padrão para todos eles.

A classe de Embeddings base em LangChain fornece dois métodos: um para realizar o embedding de documentos
e outro para embedding de uma chamada. O primeiro recebe como entrada vários textos, enquanto o último
recebe um único texto.

https://docs.langchain.com/oss/python/integrations/text_embedding
https://platform.openai.com/docs/guides/embeddings
"""

from dotenv import load_dotenv
import numpy as np
from langchain_openai import OpenAIEmbeddings

load_dotenv()

embedding_model = OpenAIEmbeddings(model='text-embedding-ada-002')

embeddings = embedding_model.embed_documents([
    'Eu gosto de cachorros',
    'Eu gosto de animais',
    'O tempo está ruim lá fora'
])

print(len(embeddings))
#print(embeddings[0][:10])
print(len(embeddings[0]))

for em in embeddings:
    print(len(em), max(em), min(em))

print('-'*100)
# print(np.dot(embeddings[0], embeddings[1]))

for i in range(len(embeddings)):
    for j in range(len(embeddings)):
        print(round(np.dot(embeddings[i], embeddings[j]), 2), end=' | ')
    print()