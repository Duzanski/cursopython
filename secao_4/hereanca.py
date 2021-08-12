class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade


class Cliente(Pessoa):
    pass


class Aluno(Pessoa):
    pass


c1 = Cliente('REinaldo', 32)
print(c1.nome)
a1 = Aluno('JOao', 52)
print(a1.nome)
