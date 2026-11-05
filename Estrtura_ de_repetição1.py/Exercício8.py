#8-	Peça ao usuário um número inteiro positivo
#  e exiba todos os números pares de forma decrescente até chegar a zero. 
# O programa deve exibir a sequência de forma organizada,
# considerando que o número de entrada pode ser par ou ímpar.

num = int(input("Insira um número positivo: "))
while num >= 0:
    if num % 2 == 0:
        print(num)
    num -= 1