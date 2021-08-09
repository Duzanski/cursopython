'''
Set é basicamente uma biblioteca porém com apenas os valores, sem as keys

- Add (adiciona)
- Update (atualiza)
- Clear (limpa)
- Discart
- Union | une)
- Intersection & (todos os elementos presentes nos dois sets)
- Difference - (elementos apenas no set da esquerda que diferem do da direita)
# Symmetric_difference ^ (elementos que estão nos dois sets porém não em ambos)
'''

# Criando set
s1 = {1, 2, 3, 4, 5}

# Ou
s2 = set()
s2.add(1)
s2.add(2)
s2.add(3)
s2.add(4)
s2.add(5)
s2.add(6)

# Removendo elemento
s2.discard(2)

# Update
s2.update('Python')  # vai adicionar letra por letra e não ordenada

# Usando set para remover elementos duplicados de uma lista
lista = [1, 2, 3, 4, 1, 1, 1, 3, 3, 2, 5, 2, 'Reinaldo', 'Reinaldo']
lista = set(lista)
print(lista)

# Union
s3 = s1.union(s2)
s3 = s1 | s2  # mesma coisa que a linha acima
print(s3)

# Intersection
s3 = s1 & s2

# Difference
s3 = s1 - s2

# Symmetric
s3 = s1 ^ s2
