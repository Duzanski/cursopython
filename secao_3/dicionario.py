'''
Dicionário - é basicamente uma lista porém eu mesmo controlo o índice

lista = []
tupla = ()
dicionario = {}
'''

# Outro jeito de criar um dicionário
d2 = dict(chave1='Valor da chave', chave2='Valor da outra chave')

d1 = {'chave1': "valor da chave"}

# Adicionando novo valor
d1['nova chave'] = 'Valor da nova chave'

# Outra forma de adicionar/atualizar valor
d1.update({'chave1': 'reinaldo'})

# Apagando item
del d1['chave1']

# Checando valores no dicionário
print('chave1' in d1)
print('chave1' in d1.keys())  # basicamente mesma coisa que a linha acima
print('valor da chave' in d1.values())  # confere os valores

# Acessando todos os items
for k, v in d1.items():
    print(k, v)

# Dicionário dentro de dicionário
clientes = {
    'cliente1': {
        'nome': 'Reinaldo',
        'sobrenome': 'Duzanski',
    },
    'cliente2': {
        'nome': 'Silva',
        'sobrenome': 'Joao',
    },
    'cliente3': {
        'nome': 'Teste',
        'sobrenome': 'Fulano',
    },
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')

# Fazendo uma cópia
copia = d1.copy()
