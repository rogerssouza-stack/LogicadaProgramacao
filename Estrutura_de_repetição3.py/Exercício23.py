qtdTransacao = 0
valorTransacaoVista = 0
valorTransacaoPrazo = 0
while qtdTransacao < 15:
    cod = int(input("Insira o código do tipo de transação: "))
    valor = int(input("Insira o valor da transação: "))
    qtdTransacao += 1
    if cod == 1:
        valorTransacaoVista += valor
        valorTotalVista = valorTransacaoVista
    else:
        valorTransacaoPrazo += valor
        valorTotalPrazo = valorTransacaoPrazo
    valorTotal = valorTransacaoVista + valorTransacaoPrazo
    valorPrestacaoPrazo = valorTransacaoPrazo / 3
print("O valor total das compras à vista é de R$", valorTransacaoVista)
print("O valor total das compras a prazo é de R$", valorTransacaoPrazo)
print("O valor da primeira prestação da transação a prazo é de R$", valorPrestacaoPrazo)
print("O valor total das compras efetuadas é de R$", valorTotal)