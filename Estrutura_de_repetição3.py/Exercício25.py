qtdProduto1 = 0
qtdProduto2 = 0
qtdProduto3 = 0
qtdProduto4 = 0
valorPagar = 0
valorTotal = 0

while True:
    cod = int(input("Digite o código do produto (0 para encerrar): "))

    if cod == 0:
        break

    qtdProduto = int(input("Digite a quantidade de produtos: "))

    if cod == 100 or cod == 103:
        preco = 1.20

    elif cod == 101 or cod == 104:
        preco = 1.30

    elif cod == 102:
        preco = 1.50

    elif cod == 105:
        preco = 1.00

    else:
        print("Código inválido")
        continue

    valorPagar = qtdProduto * preco
    valorTotal += valorPagar

    print("O valor a pagar pelo item é de R$", valorPagar)

print("O valor total do pedido é de R$", valorTotal)