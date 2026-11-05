qtdNum = 0
qtdValor = 0
while qtdNum < 80:
    num = int(input("Insira um número: "))
    qtdNum += 1
    if num >= 10 and num <= 150:
        qtdValor += 1
print("A quantidade de números no intervalo de 10 e 150 é: ", qtdValor)