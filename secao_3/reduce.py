from dados_map import pessoas, produtos, lista
from functools import reduce

# Somando os valores da lista
soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
print(soma_lista)

# Somando os valores dos precos
precos_soma = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
print(round(precos_soma, 2))
