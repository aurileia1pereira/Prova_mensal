
class Pagamento:
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def calcular_valor_final(self):
        return self._valor



class PagamentoDebito(Pagamento):
    def calcular_valor_final(self):
        return self.valor


class PagamentoPix(Pagamento):
    def calcular_valor_final(self):
        return self.valor * 0.95


class PagamentoDinheiro(Pagamento):
    def calcular_valor_final(self):
        return self.valor * 0.97


class PagamentoCartao(Pagamento):
    def calcular_valor_final(self):
        return self.valor * 1.05
