contador1 = 0
contador2 = 0
contador3 = 0
contador4 = 0
contador5 = 0
codProduto = 1
while codProduto != 0:
    codProduto = int(input("Insira o código do produto: "))
    if codProduto == 0:
      totalProdutos = contador1 + contador2 + contador3 + contador4 + contador5
      print("O total de produtos classificados é: ", totalProdutos)
      print("O número de produtos classificados como alimento não-perecível é: ", contador1)
      print("O número de produtos classificados como alimento perecível é: ", contador2)
      print("O número de produtos classificados como vestuário é: ", contador3)
      print("O número de produtos classificados como higiene pessoal é: ", contador4)
      print("O número de produtos classificados como limpeza e utensílios domésticos é: ", contador5)
      break
    if codProduto == 1:
        contador1 += 1
    elif codProduto < 5:
        contador2 += 1
    elif codProduto < 7:
        contador3 += 1
    elif codProduto == 7:
        contador4 += 1
    elif codProduto < 16:
        contador5 += 1
    else:
        print("O código é inválido, portanto não é possível prosseguir, insira outro código.")