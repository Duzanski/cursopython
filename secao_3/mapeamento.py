from dados_map import produtos, pessoas, lista

# Pegando dados da lista e multiplicando
nova_lista = map(lambda x: x*2, lista)
# mesma coisa que o cod acima porem usando list comprehension
nova_lista2 = {x * 2 for x in lista}

# Trabalhando dicionário pegando so os preços
precos = map(lambda p: p['preco'], produtos)
for v in precos:
    print(v)

# Aumentando o preço em 5%


def aumenta_preco(produto):
    produto['preco'] = round(produto['preco'] * 1.05, 2)
    return produto


precos_novos = map(aumenta_preco, produtos)
for v in precos_novos:
    print(v)
