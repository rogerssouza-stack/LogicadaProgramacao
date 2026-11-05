codigoCidade = 0; numeroVeiculos = 0; numeroAcidentes = 0
maiorAcidente = 0
cidadeMaior = 0
cidadeMenor = 0
somaTodasCidades = 0
somaSC = 0
qtdSC = 0
somaRS = 0
qtdRS = 0
somaPR = 0
qtdPR = 0
acidentePR = 0
acidenteRS = 0
acidenteSC = 0
menorAcidente = float("inf")
for contador in range(1,12):
    codigoCidade = int(input("Digite o código da cidade: "))
    numeroVeiculos = int(input("Digite o número de veículos: "))
    numeroAcidentes = int(input("Digite o número de acidentes: "))
    if numeroAcidentes > maiorAcidente:
        maiorAcidente = numeroAcidentes
        cidadeMaior = codigoCidade
    if numeroAcidentes < menorAcidente:
        menorAcidente = numeroAcidentes
        cidadeMenor = codigoCidade
    somaTodasCidades += numeroVeiculos
    if codigoCidade >= 11 and codigoCidade <= 14:
        somaSC += numeroVeiculos
        qtdSC += 1 
    if codigoCidade >= 21 and codigoCidade <= 24:
        somaRS += numeroVeiculos
        qtdRS += 1
    if codigoCidade >= 31 and codigoCidade <= 34:
        somaPR += numeroVeiculos
        qtdPR += 1
print("A média de veículos no Brasil é: ", (somaTodasCidades / 12))
print("A média de veículos em Santa Catarina é: ", (somaSC / qtdSC))
print("A média de acidente em Santa Catarina é: ", numeroAcidentes / 4)
print("A média de veículos no Rio Grande do Sul é: ", (somaRS / qtdRS))
print("A média de acidente no Rio Grande do Sul é: ", numeroAcidentes / 4)
print("A média de veículos no Paraná é: ", (somaPR / qtdPR))
print("A média de acidente no Paraná é: ", numeroAcidentes / 4)