
from datetime import datetime
from item_venda import ItemVenda


class Venda:

    _total_vendas = 0

    def __init__(self):
        self._data = datetime.now()
        self._valor_total = 0.0
        self._itens = []
        self._pagamento = None

        Venda._total_vendas += 1

    @property
    def itens(self):
        return self._itens

    @property
    def valor_total(self):
        return self._valor_total

    def calcular_total(self):
        self._valor_total = 0.0

        for item in self.itens:
            self._valor_total += item.calcular_subtotal()

        return self._valor_total

    def adicionar_item(self, produto, quant):
        if quant <= 0:
            return False

        if not produto.decrementar_estoque(quant):
            return False

        item = ItemVenda(produto, quant)
        self._itens.append(item)

        self.calcular_total()

        return True

    def remover_item(self, produto):
        for item in self.itens:
            if item.produto == produto:
                produto.estoque += item.quantidade

                self._itens.remove(item)
                self.calcular_total()

                return True

        return False

    def finalizar_venda(self, pagamento):
        if not self.itens:
            return False

        self._pagamento = pagamento(self.calcular_total())

        return self._pagamento.calcular_valor_final()

    @staticmethod
    def get_total_vendas():
        return Venda._total_vendas
