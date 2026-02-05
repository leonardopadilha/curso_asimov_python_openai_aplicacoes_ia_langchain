from langchain.document_loaders.base import BaseLoader
from langchain.schema import Document

class MyCustomLoader(BaseLoader):
    def __init__(self, source):
        self.source = source # Fonte de dados, como um arquivo ou URL

    def load(self):
        # Lógica para carregar os dados da fonte
        documents = []
        with open(self.source, 'r', encoding='utf-8') as file:
            content = file.read()
            # Criar um documento com o conteúdo e metadados
            documents.append(Document(page_content=content, metadata={"source": self.source}))
        return documents

# Criar uma instância do loader
loader = MyCustomLoader('./arquivos/arquivo.txt')
documentos = loader.load()

# Verificar o conteúdo carregado
for doc in documentos:
    print(doc.page_content) # Exibir o conteúdo do documento
    print(doc.metadata) # Exibir os metadados do documento 
