'''
Quando uma classe pertence a outra e quando um objeto que pertence a outro
for deletado tudo é perdido
'''


class Cliente:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
        self.endereco = []

    def insere_endereco(self, cidade, estado):
        self.endereco.append(Endereco(cidade, estado))

    def lista_endereco(self):
        for endereco in self.endereco:
            print(endereco.cidade, endereco.estado)


class Endereco:
    def __init__(self, cidade, estado) -> None:
        self.cidade = cidade
        self.estado = estado


cliente1 = Cliente("REinaldo", 32)
cliente1.insere_endereco('Belo Horizonte', 'MG')

cliente2 = Cliente('Maria', 63)
cliente2.insere_endereco('Joaquim Tavora', 'PR')
cliente2.lista_endereco()
