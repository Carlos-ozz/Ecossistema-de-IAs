from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage

#IMPORTAR API KEY DO ARQUIVO .ENV
load_dotenv()
CALIA_KEY=os.getenv("API_KEY_CALIA")

#CONFIGURAR OS PARAMETROS DO LLM
calia_llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.5,
    api_key=CALIA_KEY
)

#IMPORTAR PROMPT QUE DA CONTEXTO PARA MINHA IA
from prompts import CALIA_PROMPT

#LOOP PARA CONVERSAR COM O LLM
print("CALIA iniciada. Digite 'sair' para encerrar.")
while True:
    pergunta = str(input("Você: "))
    if pergunta.lower() in ["sair", "exit"]:
        print("CALIA: Até logo, Carlos 💜")
        break

    resposta = calia_llm.invoke([
        SystemMessage(content=CALIA_PROMPT),
        HumanMessage(content=pergunta)
    ])
    print(resposta.content)