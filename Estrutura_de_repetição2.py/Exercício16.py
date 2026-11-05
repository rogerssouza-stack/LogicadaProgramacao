num = 0
somaPositivos = 0
somaNegativos = 0
numPar = 0
numImpar = 0

while True:
    num = int(input("Insira um número: "))
    if num == 0:
        somaTotal = somaPositivos + somaNegativos
        print("A soma dos números positivos é: ", somaPositivos)
        print("A soma dos números negativos é: ", somaNegativos)
        print("A soma total dos números é: ", somaTotal)
        break
    elif num > 0:
        somaPositivos += num
    else:
        somaNegativos += num