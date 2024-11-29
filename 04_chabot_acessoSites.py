import re

from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader('https://www.guialagos.tur.br/cidades/arraial-do-cabo/')
lista_documentos = loader.load()

documento = ''
for doc in lista_documentos:
  documento += doc.page_content
# print (documento)
# documento_sem_espacos = ''.join(documento.split())
documento_sem_espacos = re.sub(r'\s+', ' ', documento)

print(documento_sem_espacos)