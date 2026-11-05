mediaIdade = 0
idade = 0
contador = 0
idadeTotal = 0

while idade >= 0:
    idade = int(input("Insira sua idade: "))
    if idade >= 0:
        idadeTotal += idade
        contador += 1
        mediaIdade = idadeTotal / contador
print("A média das idades é: ", mediaIdade)