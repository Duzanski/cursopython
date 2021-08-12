from os import read, write
import os
import json

# os.remove('teste.txt') removerá o arquivo

# Usando 'a' da um append ao invés de apagar td e criar novamente
file = open('teste.txt', 'w+')
file.write('Linha 1 \n')
file.write('Linha 2\n')
file.write('Linha 3 \n')
file.write('Linha 4 \n')
# file.close()

# Voltando 'cursor' para primeira linha e lendo o arquivo
file.seek(0, 0)
print(file.read())

# Lendo linha por linha
file.seek(0, 0)
print('**************')
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')

# Jogando linha por linha em uma lista
file.seek(0, 0)
print('**************')
print(file.readlines())
# Lendo
file.seek(0, 0)
for l in file.readlines():
    print(l)
# OU
for linha in file:
    print(linha)
file.close()

# Melhor jeito de utilizar arquivos
with open('teste.txt', 'w+') as file:
    file.write('Linha 1 \n')
    file.write('Linha 2\n')
    file.write('Linha 3 \n')
    file.seek(0, 0)

# Trabalhando com arquivos json
d1 = {
    'Pessoa 1': {
        'nome': 'Luiz',
        'idade': 25,
    },
    'Pessoa 2': {
        'nome': 'João',
        'idade': 20,
    },
}
# Convertendo o dicionário em json
d1_json = json.dumps(d1, indent=True)

# Criando o arquivo json
with open('abc.json', 'w+') as file:
    file.write(d1_json)
# Lendo o json e transformando em dicionario
with open('abc.json', 'r') as file:
    d2_json = file.read()
    d2_json = json.loads(d2_json)
