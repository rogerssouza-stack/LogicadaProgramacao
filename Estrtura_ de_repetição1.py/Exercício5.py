numPar = 0
qtdPar = 0
mediaPar = 0
while True:
    num = int(input("Insira um número: "))
    if num == 0:
        break
    elif num % 2 == 0:
        numPar += num
        qtdPar += 1
        mediaPar = numPar / qtdPar
    else:
        print("O número é ímpar")