'''
Gerando e imprimindo contador
'''
from itertools import count

contador = count(start=1, step=2)

for valor in contador:
    print(valor)
    if valor >= 10:
        break


# Adicionando índices em uma lista com contrador
lista = ['Reinaldo', 'Maria', 'João', 'José']
lista = zip(contador, lista)
print(list(lista))
