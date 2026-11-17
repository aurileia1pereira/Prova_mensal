
class Produto:
    def __init__(self, descricao, preco_unitario, estoque):
        self._descricao = descricao
        self._preco_unitario = preco_unitario
        self._estoque = estoque

    @property
    def descricao(self):
        return self._descricao

    @property
    def preco_unitario(self):
        return self._preco_unitario

    @property
    def estoque(self):
        return self._estoque

    @estoque.setter
    def estoque(self, valor):
        self._estoque = valor

    def decrementar_estoque(self, quant):
        if quant <= 0:
            return False

        if quant > self.estoque:
            return False

        self.estoque -= quant
        return True
