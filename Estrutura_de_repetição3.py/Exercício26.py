qtdParcela = 0
juros = 0
valorDivida = 0
valorParcela = 0
valor = 0
while True:
    qtdParcela = int(input("Insira a quantidade de parcelas: "))
    valor = float(input("Insira o valor da dívida: "))
    if qtdParcela <= 0:
        print("Quantidade de parcelas é: ", qtdParcela,)
        print("O valor da parcela é de: ", valorParcela)
        print("O valor total da dívida é de: ", valorDivida)
        print("O valor dos juros é de: ", juros)
        break
    elif qtdParcela == 3:
        juros = valor * 0.10
        valorDivida = valor + juros
        valorParcela = (valor + juros) / qtdParcela
    elif qtdParcela == 6:
        juros = valor * 0.15
        valorDivida = valor + juros
        valorParcela = (valor + juros) / qtdParcela
    elif qtdParcela == 9:
        juros = valor * 0.20
        valorDivida = valor + juros
        valorParcela = (valor + juros) / qtdParcela
    elif qtdParcela == 12:
        juros = valor * 0.25
        valorDivida = valor + juros
        valorParcela = (valor + juros) / qtdParcela
    else:
        print("Quantidade de parcelas inválida. Por favor, insira 3, 6, 9 ou 12 parcelas.")
        continue