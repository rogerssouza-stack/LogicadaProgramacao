temperatura = 0
qtdValidas = 0
temp5 = 0
temp10 = 0
tempMaior = None
totalDigitado = 0
temp20_80 = 0
while True:
    temperatura = float(input("Insira a temperatura (ou 999 para encerrar): "))
    if temperatura == 999:
        break
    totalDigitado += 1
    if temperatura < -50 or temperatura > 150:
        continue
    qtdValidas += 1
    if temperatura >= 20 and temperatura <= 80:
        temp20_80 += 1
    if temperatura % 5 == 0:
        temp5 += 1
    if temperatura % 10 != 0: 
        temp10 += 1
    if tempMaior == None or temperatura > tempMaior:
        tempMaior = temperatura
if totalDigitado > 0:
    percentualValidas = (qtdValidas / totalDigitado) * 100
else:
    percentualValidas = 0
print("A quantidade de temperaturas válidas é: ", qtdValidas)
print("A maior temperatura é: ", tempMaior)
print("O percentual de temperaturas válidas sobre o total digitado é: ", percentualValidas, "%")