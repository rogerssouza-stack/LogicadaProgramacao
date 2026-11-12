qtdNum = 0
qtdNum3 = 0
soma_pares = 0
while qtdNum < 50:
    num = int(input("Insira um número:"))
    qtdNum += 1
    if num % 3 == 0:
        qtdNum3 += 1
    if num % 2 == 0:
        soma_pares += num

print("A quantidade de números múltiplos de 3 é: ", qtdNum3)
print("A soma dos números pares é: ", soma_pares)