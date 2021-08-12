'''
Classes que podem trabalhar entre si porem sao independentes
'''


class Escritor:
    def __init__(self, nome) -> None:
        self.__nome = nome
        self.__ferramenta = None

    @property
    def nome(self):
        return self.nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta


class Caneta:
    def __init__(self, marca) -> None:
        self.__marca = marca

    @property
    def marca(self):
        return self.marca

    def escrever(self):
        print('Caneta escrevendo')


class MaquinaDeEscrever:
    def escrever(self):
        print('Maquina escrevendo')


escritor = Escritor('Joao')
caneta = Caneta('BIc')

escritor.ferramenta = caneta
escritor.ferramenta.escrever()
