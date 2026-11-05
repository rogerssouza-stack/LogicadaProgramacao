#Foi feita uma pesquisa de audiência de canal de TV em várias casas de uma certa cidade, em um determinado dia. 
# Para cada casa visitada foi fornecido o
#número do canal (4, 5, 7, 12) e o número de pessoas que estavam assistindo a ele naquela casa. 
#Se a televisão estivesse desligada, nada seria anotado,
#ou seja, esta casa não entraria na pesquisa. Faça um Programa que:
#leia um número indeterminado de dados, isto é, o número do canal e o
#número de pessoas que estavam assistindo;
#calcule e imprima a porcentagem de audiência em cada canal. Para encerrar
#a entrada de dados, digite o número do canal zero.
pessoas4 = 0
pessoas5 = 0
pessoas7 = 0
pessoas12 = 0
canal = 0
audienciaTotal = 0
audiencia4 = 0
audiencia5 = 0
audiencia7 = 0
audiencia12 = 0
num = 0
while True:
    canal = int(input("Insira o número do canal: "))
    pessoas = int(input("Insira o número de pessoas assistindo: "))
    num = int(input("Indique se a TV esta ligada digitando 1 se estiver e 0 se não estiver: "))
    if canal == 0:
        audienciaTotal = pessoas4 + pessoas5 + pessoas7 + pessoas12
        audiencia4 = (pessoas4 / audienciaTotal) * 100
        audiencia5 = (pessoas5 / audienciaTotal) * 100
        audiencia7 = (pessoas7 / audienciaTotal) * 100
        audiencia12 = (pessoas12 / audienciaTotal) * 100
        print("A audiencia do canal 4 é de ", audiencia4, "%")
        print("A audiencia do canal 5 é de ", audiencia5, "%")
        print("A audiencia do canal 7 é de ", audiencia7, "%")
        print("A audiencia do canal 12 é de ", audiencia12, "%")
        break
    elif num == 1 and canal == 4:
        pessoas4 += pessoas
    elif num == 1 and canal == 5:
        pessoas5 += pessoas
    elif num == 1 and canal == 7:
        pessoas7 += pessoas
    elif num == 1 and canal == 12:
        pessoas12 += pessoas
    else:
        print("Inválido")