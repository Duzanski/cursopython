class Pessoa:
    ano_atual = 2021

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, alimento):
        if self.comendo:
            print(f'já está comendo')
            return
        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True

    @classmethod
    def por_ano_nasc(cls, nome, ano_nasc):
        idade = cls.ano_atual - ano_nasc
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        return 1235

    # Criando um getter
    @property
    def nome(self):
        return self._nome

    # Criando um setter
    @nome.setter
    def nome(self, valor):
        self._nome = valor
