from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

load_dotenv()

os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')

chat = ChatGroq(model='llama-3.1-70b-versatile')

resposta = chat.invoke('Olá, qual é o seu nome?')
print(resposta.content)