'''
Operador ternário
'''
logged_user = True
msg = 'Usuários logado.' if logged_user else 'Usuário precisa logar.'
print(msg)

# Verifica maior idade
idade_minima = 18
maior_idade = idade_minima >= 18

msg = 'Pode acessar.' if maior_idade else 'Menor de idade'
print(msg)

# Operador OR

a = 0
b = None
c = False
d = []
e = {}
f = 2

# Para no primeiro True que encontrar
variavel = a or b or c or d or e or f
print(variavel)
