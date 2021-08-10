'''
Basicamente igual try/catch do java
'''

# Tratando a exceção
try:
    print(a)
except NameError as erro:
    print('Deu ruim')
except Exception as erro:
    print('Pega qualquer erro no codigo')
else:
    print('Bloco executado com sucesso')
finally:
    print('Executa independente de erro ou não')

# Tratando uma execeção e relançando-a


def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        print('Log', error)
        raise  # "Levanta" a exceção novamente

        # raise ValueError('meu erro bla bla') - criando meu próprio erro
try:
    print(divide(2, 0))
except ZeroDivisionError as error:
    print(error)
