pec = 0
limiteE1 = 0
capacidade = 0
sobraPec = 0
pecE1 = 0
ciclo = 0
pec = int(input("Insira o número de peças acumuladas para o processamento: "))
limiteE1 = int(input("Insira o limite de peça que a estação suporta: "))
capacidade = float(input("Insira quantos porncento da capacidade máxima ela vai operar: "))
while True:
    if limiteE1 < pec:
        ciclo += 1
        sobraPec = limiteE1 - pec
        pecE1 = sobraPec
    else:
        limiteE1 = pecE1
    if capacidade >= 90 and ciclo >= 5:
        print("Máquina com problema parada forçada.")