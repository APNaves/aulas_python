from funcao_calcular_idade import calcular_idade
import json

arquivo = open("arquivo.json", "r")
lista = list(json.load(arquivo))

for dicionario in lista:
    nome = dicionario["nome"]
    idade = dicionario["nascimento"]

    idade = calcular_idade(idade)
    
    if idade == -1:
        print('invalida\n')
        continue

    print('\n')
    print(f"\nO seu nome é {nome}, a sua idade é {idade}")

pergunta = input('Deseja adcionar uma pessoa a lista? \n')

if pergunta.upper() == 'S':
    nome = input('Qual o nome da nova pessoa? \n')
    nascimento = input('Qual a data de nascimento da nova pessoa? \n')

    pessoa_nova = {
        "nome" : nome,
        "nascimento" : nascimento
    }
    lista.append(pessoa_nova)

print('fim!')

with open('arquivo.json', 'w+') as f:
    f.write(json.dumps(lista, indent=4))
