'''
Utilizado para otimização de código
'''
l1 = [1, 2, 3, 4, 5]
l2 = [variavel for variavel in l1]  # estou apensa iterando a lista

# Multiplicando cada elemento da lista
l3 = [v * 2 for v in l1]
print(l3)

# Trocando 'a' por @
lista = ['reinaldo', 'maria']
l4 = [v.replace('a', '@') for v in lista]
print(l4)

# Pegando números divisiveis por 2
l5 = list(range(100))
divi = [v for v in l5 if v % 2 == 0]
print(divi)

# Utilizando else
divi2 = [v if v % 3 == 0 else 'Não é' for v in l5]
print(divi2)
