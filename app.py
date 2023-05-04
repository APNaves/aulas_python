from funcao_calcular_idade import calcular_idade 
import json

arquivo = open('arquivo.json', 'r')
novo_dicionario = list(json.load(arquivo))

novo_dicionario = ({"nome":"Vlad", "nascimento":"01/11/1111"})

for i in dicionario:
    nome =  i['nome']

    if nome.lower() == "zero" or nome == "0":
        continue

    nascimento = i['nascimento']

    idade = calcular_idade(nascimento)
    
    if idade < 0:
        continue

    print(nome, idade)

print("FIM")

with open("arquivo.json", "w") as f:
    f.write(json.dump(novo_dicionario, indent=4))
