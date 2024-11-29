import os
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')

chat = ChatGroq(model='llama-3.1-70b-versatile')

def resposta_bot(mensagens):

  mensagens_modelo = ['system', 'Você é um assistente pessoal chamado Cristina. Você deve responder as perguntas dos usuários e ajudá-los a resolver problemas.']
  mensagens_modelo += mensagens
  template = ChatPromptTemplate.from_messages(mensagens_modelo)
  chain = template | chat

  return chain.invoke({}).content

print('Bem-vindo ao Assitente pessoal')

mensagens = []
while True:
  pergunta = input('Usuario: ')
  if pergunta.lower() == 'x':
    break
  mensagens.append(('user', pergunta))
  resposta = resposta_bot(mensagens)
  mensagens.append(('assistant', resposta))
  print(f'Bot: {resposta}')

print('Muito obrigado por usar o Assitente pessoal')
print(mensagens)