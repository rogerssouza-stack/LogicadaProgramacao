pontuacao1 = 0
pontuacao2 = 0

while True:
    num = int(input("Insira o número do jogador que pontuou: "))
    if num == 1:
        pontuacao1 += 1
    if pontuacao1 >= 21 and pontuacao1 - pontuacao2 >= 2:
        print("O jogodor 1 vence.")
        break
    if num == 2:
        pontuacao2 += 1
    if pontuacao2 >= 21 and pontuacao2 - pontuacao1 >= 2: 
        print("O jogador 2 vence.")
        break