numNegativo = 0

while True:
    num = int(input("Insira um número: "))
    if num < 0:
        numNegativo += 1
        print(numNegativo)
    elif num == 0:
        break