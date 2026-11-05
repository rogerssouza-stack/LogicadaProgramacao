import random
numMaquina = random.randint(1,50)
num = 0

for i in range(1,6):
    num = int(input("Advinhe o número entre 1 e 50: "))
    if num == numMaquina:
        print("Você acertou o número, parabéns.")
    elif num < numMaquina:
        print("O número inserido é menor.")
    elif num > numMaquina:
        print("O número inserido é maior.")
else:
    print("As tentativas acabaram o número era: ", numMaquina)