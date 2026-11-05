ciclo = 0
Temperatura = 0

Temperatura = float(input("Insira a temperatura do forno: "))
while True:
    ciclo += 1
    if Temperatura < 800:
        Temperatura += 50
        ciclo += 1
    elif Temperatura >= 800 and Temperatura < 1000:
        Temperatura += 20
    else:
        Temperatura = Temperatura
        break
print("A quantidade de ciclos para que a temperatura atigisse 1000 °C foi: ", ciclo)