#João tem 1,50 metro e cresce 2 centímetros por ano, enquanto Zé tem 1,10 metro e cresce 3 centímetros por ano. 
# Construa um algoritmo que calcule e imprima quantos anos serão necessários para que Zé seja maior que João.

altura1 = float(input("Insira sua altura em metros: "))
altura2 = float(input("Insira a segunda altura em metros: "))
ano = 0
while altura1 > altura2:
    altura1 += 0.02
    altura2 += 0.03
    ano += 1
print("A quantidade de anos necessários para Zé ultrapassar João serão: ", ano)