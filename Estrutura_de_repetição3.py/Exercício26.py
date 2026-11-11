valor = float(input("Insira um valor: "))

qtdParcelas = 1

while qtdParcelas <= 12:

    if qtdParcelas == 1:
        juros = 0
    elif qtdParcelas == 3:
        juros = valor * 0.10
    elif qtdParcelas == 6:
        juros = valor * 0.15
    elif qtdParcelas == 9:
        juros = valor * 0.20
    elif qtdParcelas == 12:
        juros = valor * 0.25

    valorDivida = valor + juros
    valorParcela = valorDivida / qtdParcelas

    print(f"Valor da dívida: R${valorDivida:.2f} - Parcelas: {qtdParcelas} - Valor da parcela: R${valorParcela:.2f} - Valor dos juros: R${juros:.2f}")

    if qtdParcelas == 1:
        qtdParcelas = 3
    elif qtdParcelas == 3:
        qtdParcelas = 6
    elif qtdParcelas == 6:
        qtdParcelas = 9
    elif qtdParcelas == 9:
        qtdParcelas = 12
    else:
        qtdParcelas = 13