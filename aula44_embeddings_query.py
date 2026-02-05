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

pergunta = 'O que é um cachorro?'
emb_query = embedding_model.embed_query(pergunta)
print(emb_query[:10])