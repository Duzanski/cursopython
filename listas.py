'''
-> Fatiamento
-> Comandos
    -> Append
    -> Insert
    -> Pop
    -> Del
    -> Clear
    -> Extend
    -> Min
    -> Max
    -> Range
'''

# Criando 'lista' e acessando valores
#         0    1    2    3
lista_ = ['A', 'B', 'C', 'D', True, 10.5]

# Fatiamento

print(lista_[:3])  # printa os 3 primeiros índices da 'lista'
print(lista_[2:])  # começa pelo índice 2 e vai até o final
# primeiro : (começo), segundo : (fim), 2 é o salteamento (pula de 2 em 2)
print(lista_[::2])
print(lista_[-1])  # pega o último da 'lista'


# Extend

l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]
l3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

l1.extend(l2)  # adiciona ao final o valores de l2 em l1
print(l1)

# Append

l2.append('b')  # insere um valor no final da 'lista'
print(l2)

# Insert

# insere no índice 0 o valor teste e desloca os outros índices
l2.insert(0, 'teste')
print(l2)

# Pop

l2.pop()  # remove o último valor da 'lista'
print(l2)

# Del

del(l3[1:3])  # remove de acordo com o índice que eu desejar
print(l3)

# Max

print(max(l3))

# Min

print(min(l3))

# Clear

l3.clear()  # limpa a 'lista'

# Jogo descubra a palavra secreta

palavra_secreta = 'perfume'
digitas = []
chances = 3

while True:
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Digite apenas uma letra')
        break
