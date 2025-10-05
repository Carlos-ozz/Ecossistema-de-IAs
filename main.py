from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from prompts import ARYA_PROMPT, LYRA_PROMPT, AUREN_PROMPT, CALIA_PROMPT, ORION_PROMPT, LYRIUS_PROMPT, VITALIS_PROMPT

#IMPORTAR API KEY DAS IAs
load_dotenv()
LYRIUS_KEY=os.getenv("API_KEY_LYRIUS")
CALIA_KEY=os.getenv("API_KEY_CALIA")
ORION_KEY=os.getenv("API_KEY_ORION")
AYRA_KEY=os.getenv("API_KEY_AYRA")
AUREN_KEY=os.getenv("API_KEY_AUREN")
LYRA_KEY=os.getenv("API_KEY_LYRA")
VITALIS_KEY=os.getenv("API_KEY_VITALIS")

#Teste para receber msg do usuário
mensagem = str(input("Digite sua mensagem: "))

 #Parametros do modelo que será usado na triagem
lyrius_llm=ChatGoogleGenerativeAI(
    model ="gemini-2.5-flash",      
    temperature = 0.3,
    api_key = LYRIUS_KEY
)

#Template de tiragem que envia o prompt e a mensagem direto para o sistema
triagem_template = ChatPromptTemplate.from_messages([
    ("system", LYRIUS_PROMPT),   
    ("user", "{mensagem}"), 
])

#Extrai apenas o conteúdo da resposta
parser = StrOutputParser() 

#Triagem que recebe a mensagem e decide qual IA vai responder
triagem_chain = triagem_template | lyrius_llm | parser 
 

os.system(f"python {triagem_chain}.py")
