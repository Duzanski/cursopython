'''
Split - Dividir uma string e transforma em lista
Join - Juntar uma lista e transforma em string
Enumerate - Enumera elementos da lista
'''
frase = 'O rato roeu a roupa do rei de roma, bla bla bla'
# Splitando por espaço
lista = frase.split(' ')

# Contando o número de vezes que a apalavra aparece na lista
for valor in lista:
    print(f'A palavra {valor} apareceu {lista.count(valor)} X na lista')

# Pegando a palavra que apareceu mais vezes
palavra = ''
contador = 0
for valor in lista:
    qtd = lista.count(valor)

    if qtd > contador:
        contador = qtd
        palavra = valor
print(f'A palavra {palavra} apareceu {contador} Xs')

# Juntando uma lista com Join usando ' ' como separador
print(lista)
nova_string = ' '.join(lista)
print(nova_string)

# Enumerate
for indice, valor in enumerate(lista):
    print(indice, valor)
