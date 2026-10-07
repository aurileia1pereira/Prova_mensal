
from datetime import datetime
from item_venda import ItemVenda


class Venda:
    def __init__(self):
        self.data = datetime.now()
        self.valor_total = 0.0
        self.itens = []

    def calcular_total(self):
        self.valor_total = 0.0

        for item in self.itens:
            self.valor_total += item.calcular_subtotal()

        return self.valor_total

    def adicionar_item(self, produto, quant):
        if quant <= 0:
            return False

        if not produto.decrementar_estoque(quant):
            return False

        item = ItemVenda(produto, quant)
        self.itens.append(item)

        self.calcular_total()

        return True

    def remover_item(self, produto):
        for item in self.itens:
            if item.produto == produto:

                produto.estoque += item.quantidade

                self.itens.remove(item)
                self.calcular_total()

                return True

        return False
