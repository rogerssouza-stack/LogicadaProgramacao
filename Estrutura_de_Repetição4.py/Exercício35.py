ciclo = 0
desgate = 0

while True:
    desgate += 7
    ciclo += 1
    if ciclo > 70:
        desgate += 10
    if desgate >= 500:
        print("A máquina quebrou")
        print("A quantidade de ciclos que a máquina durou foi: ", ciclo)
        print("O desgate final da máquina foi: ", desgate)
        break