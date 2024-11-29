import os
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_community.document_loaders import PyPDFLoader

load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')

chat = ChatGroq(model='llama-3.1-70b-versatile')

arquivo = 'arquivos\RoteiroViagemEgito.pdf'

loader = PyPDFLoader(arquivo)
lista_documentos = loader.load()
# print(lista_documentos)

arquivo = ''
for doc in lista_documentos:
  arquivo += doc.page_content

input = input('O que deseja saber sobre o Egito? ')

template = ChatPromptTemplate.from_messages([
  ('system', 'Você é um agente de turismo e precisa passar informações com base em {informacoes}'),
  ('user', '{input}')
])

chain_pdf = template | chat
resposta = chain_pdf.invoke({'informacoes': arquivo, 'input': 'Por quais cidades passar no Egito'})

print(resposta.content)