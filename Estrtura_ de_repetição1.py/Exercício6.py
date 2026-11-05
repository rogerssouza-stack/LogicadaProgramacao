num = int(input("Insira um número: "))
intervalo = int(input("Insira um intervalo para diminuir o número: "))

for i in range(num, -1, -intervalo):
    print(i)