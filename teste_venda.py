from produto import Produto
from venda import Venda
from pagamento import (
    PagamentoDebito,
    PagamentoPix,
    PagamentoDinheiro,
    PagamentoCartao
)

arroz = Produto("Arroz", 6.50, 10)

feijao = Produto("Feijão", 8.00, 5)

macarrao = Produto("Macarrão", 4.50, 8)

venda = Venda()

print("Estoque antes da venda:")

print(f"Arroz: {arroz.estoque}")

print(f"Feijão: {feijao.estoque}")

print(f"Macarrão: {macarrao.estoque}")

print("\nAdicionando itens a compra...")

if venda.adicionar_item(arroz, 2):

    print("Arroz adicionado com sucesso!")

if venda.adicionar_item(feijao, 1):

    print("Feijão adicionado com sucesso!")

if venda.adicionar_item(macarrao, 3):

    print("Macarrão adicionado com sucesso!")

print("\nTotal da venda:")

print(f"R$ {venda.calcular_total():.2f}")


print("\nEstoque apos a venda:")

print(f"Arroz: {arroz.estoque}")

print(f"Feijão: {feijao.estoque}")

print(f"Macarrão: {macarrao.estoque}")

print("\nRetirando arroz...")

if venda.remover_item(arroz):

    print("Arroz removido com sucesso!")

print("\nNovo total:")

print(f"R$ {venda.calcular_total():.2f}")

print("\nEstoque após remover o arroz:")

print(f"Arroz: {arroz.estoque}")

print("\nPAGAMENTO NO DÉBITO")

valor = venda.finalizar_venda(PagamentoDebito)

print(f"Valor final: R$ {valor:.2f}")


print("\nPAGAMENTO NO PIX")

valor = venda.finalizar_venda(PagamentoPix)

print(f"Valor final: R$ {valor:.2f}")


print("\nPAGAMENTO EM DINHEIRO")

valor = venda.finalizar_venda(PagamentoDinheiro)

print(f"Valor final: R$ {valor:.2f}")


print("\nPAGAMENTO NO CARTÃO")

valor = venda.finalizar_venda(PagamentoCartao)

print(f"Valor final: R$ {valor:.2f}")
