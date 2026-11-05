num1 = int(input("insira o número que você quer fazer a tabuada: "))
num2 = int(input("Insira o número para determinar até onde irá a tabuada: "))
print(num1)
print(num2)
for i in range(1, num2 + 1):
    resultado = num1 * i
    print(num1, "x", i, "=", resultado)