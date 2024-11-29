
# Configuração e executção do projeto
1. Renomeie o `.env.example` para `.env`
2. Adicione sua chave API da GROQ
3. Crie um ambiente virtual (se não tiver criado ainda) com o comando `python -m venv venv`
4. Inicialize o ambiente virtual Powershell `.\venv\Scripts\Activate`
5. Execute um dos projetos. Ex.: `py 08_chatbotCompleto.py`

# Bibliotecas langchain
- langchain
- - Framework para trabalhar com LLM
- langchain-groq
- - Cloud llama da Meta `https://console.groq.com/login`
- langchain-community 
- - Acessar sites externos (base de conhecimento)
- - Pode ser necessário `pip install beautifulsoup4`

# Prompts
- Prompt padrão: é o diálogo entre o diálogo e a LLM
- Prompt Template: É uma estrutura pré-definida (Escreva o artigo utilizando boas práticas de SEO...)
- - `from langchain.prompts import ChatPromptTemplate`

## Tipos de mensagens

*Principais*
- system, instruções do sistema: Você é um interprete...
- user, prompt do usuário: Traduza Olá mundo para o inglês
- assistant, usado para registrar a resposta do assistente ao usuário. Ele ajuda o modelo a manter o contexto da conversa, lembrando as respostas anteriores. Isso facilita para que o modelo continue a conversa com base no que já foi dito. Por exemplo, após o usuário perguntar algo, a resposta do assistente seria "Para fazer uma chamada de API em Python, você pode usar a biblioteca requests.

*Outros*
- Function Prompt
- Tool Prompt
- Few-Shot Prompt
- Contextual Prompt
