from funcao import calcular_idade
import json

nome = open("arquivo.json", "r")

dicionario = json.load(nome)

for i in dicionario:
    nome = i["nome"]
    idade = i["nascimento"] 
    
    idade = calcular_idade(idade)
    
    if idade == -1:
        print('invalida')
        continue

print("-"*30)
print(f"seu nome é {nome}, sua idade é {idade}")
print("-"*30)

    

print('fim!')
