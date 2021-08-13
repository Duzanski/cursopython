'''
Fornece um decorador e funções para criar automaticamente metodos
como o init, repr, eq etc
'''
from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    sobrenome: str


p1 = Pessoa('Reinaldo', 'Duzanski')
