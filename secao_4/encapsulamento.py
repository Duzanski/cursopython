class BaseDeDados:
    def __init__(self) -> None:
        self.dados = {}

    def inserir_clientes(self, id, nome):
        if 'clientes' not in self.dados:
            self.dados['clientes'] = {id: nome}
        else:
            self.dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_clientes(1, 'Reinaldo')
bd.inserir_clientes(2, 'Vini')
bd.inserir_clientes(3, 'Juliano')
bd.apaga_cliente(2)
bd.lista_clientes()