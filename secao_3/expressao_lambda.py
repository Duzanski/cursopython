'''
Lambda - função anônima
'''


def func(arg, arg2):
    return arg * arg2


def a(x, y): return x * y  # mesma coisa que a função acima


print(a(2, 2))

# Ordenando uma lista

lista = [
    ['P1', 10],
    ['P2', 60],
    ['P3', 100],
    ['P4', 25],
    ['P5', 80],
    ['P6', 13],
    ['P7', 20],
]

# Faria assim se não fosse usar lambda


def func(item):
    return item[1]


lista.sort(key=func)
print(lista)

# Usando lambda
lista.sort(key=lambda item: item[1])
print(lista)
