import os
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_community.document_loaders import YoutubeLoader

load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')

chat = ChatGroq(model='llama-3.1-70b-versatile')

url = 'https://www.youtube.com/watch?v=c-dlrlTaoFs'

loader = YoutubeLoader.from_youtube_url(
  url,
  language='pt'
)

lista_documentos = loader.load()

documento = ''

for doc in lista_documentos:
  documento += doc.page_content
# print(documento)

input = input('Informe quantas pessoas e idade das crianças: ')

template = ChatPromptTemplate.from_messages([
  ('system', 'Você é um agente de turismo e precisa passar informações com base em {informacoes}'),
  ('user', '{input}')
])

chain_youtube = template | chat
resposta = chain_youtube.invoke({'informacoes': documento, 'input': 'Sugira um roteiro de viagens para família com crianças'})

print(resposta.content)