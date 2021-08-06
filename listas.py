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

l2.pop()  # remove o último valor da lista
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
digitadas = []
chances = 3


while True:
    if chances == 0:
        print('Número de chances esgotada')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Digite apenas uma letra')
        continue
    digitadas.append(letra)

    if letra in palavra_secreta:
        print(f'A letra {letra} existe na palavra secreta')
    else:
        print(f'A letra {letra} NÃO existe na palavra secreta')
        digitadas.pop()
        chances -= 1

    palavra_secreta_temp = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in digitadas:
            palavra_secreta_temp += letra_secreta
        else:
            palavra_secreta_temp += '*'
    if palavra_secreta_temp == palavra_secreta:
        print(f'Você ganhou!!! a palavra era -> {palavra_secreta_temp}')
        break
    else:
        print(f'A palavra secreta está assim: {palavra_secreta_temp}')
