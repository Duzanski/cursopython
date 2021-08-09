from dados_map import produtos, pessoas, lista

# Pegando valores maior que 5 utilizando filter
nova_lista = filter(lambda x: x > 5, lista)

# Fazendo a mesma coisa acima porem com list comprehension
nova_lista2 = [x for x in lista if x > 5]

# Pegando produtos > que 10
prod = filter(lambda p: p['preco'] > 10, produtos)
for p in prod:
    print(p['nome'])
