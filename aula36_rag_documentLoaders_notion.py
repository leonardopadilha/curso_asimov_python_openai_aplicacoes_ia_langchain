from langchain_community.document_loaders.notion import NotionDirectoryLoader

caminho = './arquivos/notion_db'
loader = NotionDirectoryLoader(caminho)
documentos = loader.load()
print(len(documentos))
print(documentos[4].page_content)
print(documentos[4].metadata)