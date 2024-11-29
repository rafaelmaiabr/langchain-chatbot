import os
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import YoutubeLoader

load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')

chat = ChatGroq(model='llama-3.1-70b-versatile')

def resposta_bot(mensagens, documento):

  mensagens_sistema = '''Você é um assistente pessoal chamado Cristina.
  Utilize apenas as informações do documento {informacoes} para responder as perguntas do usuário. Limite sua resposta a 6000 tokens.
  '''
  mensagens_modelo = ['system', mensagens_sistema]
  mensagens_modelo += mensagens
  template = ChatPromptTemplate.from_messages(mensagens_modelo)
  chain = template | chat

  # Truncate document to fit within token limit
  max_tokens = 6000
  documento_truncado = documento[:max_tokens]
  return chain.invoke({'informacoes': documento_truncado}).content

print ('Bem-vindo ao Assistente pessoal')

texto_selecao = '''
*** Selecione uma opção ***

1 - Conteúdo de um site
2 - Conteúdo de um PDF
3 - Conteúdo de um vídeo do YouTube
'''

selecao = input(texto_selecao)


while selecao not in ['1', '2', '3']:
  selecao = input('Selecione uma opção entre 1 e 3 ou x para sair: ')


def carrega_site():
  url = input('Informe a URL do site: ')
  loader = WebBaseLoader(url)
  
  lista_documentos = loader.load()
  documento = ''

  for doc in lista_documentos:
    documento += doc.page_content
  return documento

def carrega_pdf():
  arquivo = input('Informe o caminho do arquivo PDF: ')
  loader = PyPDFLoader(arquivo)
  lista_documentos = loader.load()

  documento = ''
  for doc in lista_documentos:
    documento += doc.page_content

  return documento

def carrega_youtube():
  url = input('Informe a URL do vídeo do YouTube: ')
  loader = YoutubeLoader.from_youtube_url(
    url,
    language='pt'
  )

  lista_documentos = loader.load()
  documento = ''
  
  for doc in lista_documentos:
    documento += doc.page_content
    
  return documento

while True:
  if selecao == '1':
    documento = carrega_site()
    break
  elif selecao == '2':
    documento = carrega_pdf()
    break
  elif selecao == '3':
    documento = carrega_youtube()
    break
  elif selecao == 'x':
    break

mensagens = []
while True:
  pergunta = input('Usuario: ')
  if pergunta.lower() == 'x':
    break
  mensagens.append(('user', pergunta))
  resposta = resposta_bot(mensagens, documento)
  mensagens.append(('assistant', resposta))
  print(f'Bot: {resposta}')

print('Muito obrigado por usar o Assitente pessoal')
print(mensagens)
