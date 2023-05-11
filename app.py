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
    return ler_arquivo()

@app.get("/arquivo")
def ler_arquivo():
    from funcao_calcular_idade import calcular_idade
    import json
    
    arquivo = open("arquivo.json", "r")
    lista = list(json.load(arquivo))

    return lista
    texto = ""

    for dicionario in lista:
        nome = dicionario["nome"]
        idade = dicionario["nascimento"]

        idade = calcular_idade(idade)
        
        if idade == -1:
            return "Idade Invalida"
        
        texto += f"O seu nome é {nome}, a sua idade é {idade}"
    
    return texto
  
#instalar uvicorn, utilazando pip install uvicorn
#para iniciar o uvicorn, digitar uvincorn no prompt ou digite no prompt python -m uvicorn
#utilizar pra o serviço do atualizar conforme o arquivo for modificado python -m uvicorn app:app --reload
