import os
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')

template = ChatPromptTemplate.from_messages(
  [
    ('system', 'Você é um interprete e sempre deve traduzir uma expressão para o idioma especificado e com uma piada sobre o assunto.'),
    ('user', 'Traduza {expressao} para o idioma {idioma}'),
  ]
)

print(template)

template.invoke({'expressao':'Beleza?', 'idioma':'inglês'})
chat = ChatGroq(model='llama-3.1-70b-versatile')

chain = template | chat

resposta = chain.invoke({'expressao':'Levar meu cão para passear', 'idioma':'inglês'})
print(resposta.content)

