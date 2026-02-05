from langchain_community.document_loaders.web_base import WebBaseLoader

url = 'https://hub.asimov.academy/blog/autogen-agentes-autonomos-com-ia/'
loader = WebBaseLoader(url)
documents = loader.load()
print(documents[0].page_content[:1000])