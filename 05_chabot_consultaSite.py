import re
import os
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader

load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')
os.environ['USER_AGENT'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'

chat = ChatGroq(model='llama-3.1-70b-versatile')

template = ChatPromptTemplate.from_messages([
  ('system', 'Você é um agente de turismo e precisa passar informações com base em {documentos_informados}')
])

loader = WebBaseLoader('https://www.guialagos.tur.br/cidades/arraial-do-cabo/')
lista_documentos = loader.load()
documento = ''
for doc in lista_documentos:
  documento += doc.page_content

# Remover múltiplos espaços em branco e quebras de linha
documento_sem_espacos = re.sub(r'\s+', ' ', documento)

chain = template | chat
resposta = chain.invoke({
  'documentos_informados': documento_sem_espacos,
  'input': 'Sugira um roteiro de viagens'
})

print(resposta.content)