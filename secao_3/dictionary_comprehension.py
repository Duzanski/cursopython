lista = [
    ('chave', 'valor'),
    ('chave2', 'valor2'),
]

d1 = {x: y for x, y in lista}  # outra forma de fazer um casting
d1 = {x.upper(): y for x, y in lista}
print(d1)
