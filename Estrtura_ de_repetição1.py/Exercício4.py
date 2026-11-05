filhos = 0
salario = 0
somaFilhos = 0
somaSalarios = 0
mediaSalario = 0
mediaFilhos = 0
qtdSalarios = 0
qtdFamilias = 0
maiorSalario = 0
pop = 0
qtd100 = 0
while True:
    salario = float(input("Insira o salário: "))
    if salario < 0:
        break
    filhos = int(input("Insira o número de filhos: "))
    if salario >= 0 and filhos >= 0:
        pop += 1
        qtdSalarios += 1
        somaFilhos += filhos
        somaSalarios += salario
        mediaSalario = somaSalarios / qtdSalarios
        qtdFamilias += 1
        mediaFilhos = somaFilhos / qtdFamilias
        if salario > maiorSalario:
            maiorSalario = salario
        if salario <= 100:
            qtd100 += 1
percentual = (qtd100 / pop) * 100
print("A média de salário da população é: ", mediaSalario)
print("A média de filhos da população é: ", mediaFilhos)
print("O maior salário da população é: ", maiorSalario)
print("O percentual de pessoas com salário até R$100,00 é: ", percentual,"%")