'''
Funções - Def
Args
kwargs
'''

# Def


# quando uso None não sou obrigado a enviar o argumento
def saudacao(msg='Olá', nome='usuário', sobrenome=None):
    print(msg, nome)


saudacao()
saudacao('oi', 'reinaldo')
saudacao(nome='oi', msg='reinaldo')

# Args - quando não delimito o número de parâmetros


def func(*args):
    print(args)
    print(args[0])  # pega o primeiro
    print(args[-1])  # pega o último


func(1, 2, 3, 4, 5)

# Kwargs - argumentos nomeados


def func(*args, **kwargs):
    print(args)
    print(args[0])  # pega o primeiro
    print(args[-1])  # pega o último
    print(kwargs['nome'])
    print(kwargs.get('nome'))


func(1, 2, 3, 4, 5, nome='reinaldo', sobrenome='duzanski')
