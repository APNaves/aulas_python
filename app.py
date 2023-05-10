#instalar o fastapi, pelo comando pip install fastapi
from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = "*",
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.get("/")
def ola_mundo():
    return "Olá Mundo"
  
#instalar uvicorn, utilzando pip install uvicorn
#para iniciar o uvicorn, digitar uvincorn no prompt ou digite no prompt python -m uvicorn app:app
#utilizar pra o serviço do atualizar conforme o arquivo for modificado python -m uvicorn app:app --reload
