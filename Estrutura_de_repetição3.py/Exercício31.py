#Simulação de Crescimento Populacional com Evento Crítico
#Duas populações A e B crescem anualmente:
#A cresce 3% ao ano
#B cresce 1,5% ao ano
#A cada 5 anos ocorre uma crise que reduz ambas em 7%.
#Determine em quantos anos A ultrapassa B, considerando valores iniciais informados pelo usuário.

populacaoA = float(input("informe a população A: "))
populacaoB = float(input("informe a população B: "))
anos = 0

while populacaoA <= populacaoB:
    populacaoA += populacaoA * 0.03
    populacaoB += populacaoB * 0.015
    anos += 1

    if anos % 5 == 0:
        populacaoA -= populacaoA * 0.07
        populacaoB -= populacaoB * 0.07

print("A população A ultrapassará a população B em", anos, "anos.")