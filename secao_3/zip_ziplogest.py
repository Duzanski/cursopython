'''
Assimilando duas listas
'''
from itertools import zip_longest, count

indice = count()
cidades = ['Paraná', 'São Paulo', 'Belo Horizonte', 'Porto Alegre']
estados = ['PR', 'SP', 'BH']

cidades_estados = zip(estados, cidades)
for valor in cidades_estados:
    print(valor)

# Como na lista cidades tenho mais info que a estados posso usar a zip longest para pegar tds os valores e ainda setar valores padrao
cidades_estados = zip_longest(estados, cidades)
for valor in cidades_estados:
    print(valor)

# Colocando indice
cidades_estados = zip(indice, estados, cidades)
for indice, estado, cidade in cidades_estados:
    print(indice, estado, cidade)
