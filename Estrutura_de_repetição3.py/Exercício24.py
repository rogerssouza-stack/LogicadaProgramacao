#Cada espectador de um cinema respondeu a um questionário no qual constava sua idade e a sua 
#opinião em relação ao filme: ótimo=3, bom=2, regular=1. 
#Faça um programa que receba a idade e a opinião de 15 espectadores e que calcule e mostre:
#A média das idades das pessoas que responderam ótimo
#A quantidade de pessoas que respondeu regular
#A percentagem de pessoas que respondeu bom entre todos os espectadores analisados
qtdAvaliacao = 0
avaliaOtimo = 0
idadeOtimo = 0
avaliaRegular = 0
avaliaBom = 0
idade = 0
while qtdAvaliacao < 15:
    idade = int(input("insira sua idade: "))
    avaliacao = int(input("Insira sua avaliação sobre o filme: "))
    qtdAvaliacao += 1
    if avaliacao == 3:
        avaliaOtimo += 1
        idadeOtimo += idade
        mediaIdadeOtimo = idadeOtimo / avaliaOtimo
    elif avaliacao == 1:
        avaliaRegular += 1
    elif avaliacao == 2:
        avaliaBom += 1
    else:
        print("Inválido")
porcenAvaliaBom = (avaliaBom / (avaliaOtimo + avaliaRegular + avaliaBom)) * 100
print("A média das idades das pessoas que responderam ótimo é", mediaIdadeOtimo, "Anos")
print("A quantidade de pessoas que respondeu regular é", avaliaRegular, "pessoas")
print("A porcentagem de pessoas que responderam bom entre todos é de", porcenAvaliaBom)