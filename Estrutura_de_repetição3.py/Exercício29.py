cliente = 0
soma_idade = 0
total_bom = 0
total_pessimo = 0
total_excelente = 0
while cliente < 40:
    avaliacao = int(input("Digite a avaliação do cliente (1- péssimo, 2- regular, 3- bom, 4- excelente): "))
    idade = int(input("Digite a idade do cliente: "))

    if avaliacao == 4:
        cliente += 1
        total_excelente += 1
        soma_idade += idade
        media_idade = soma_idade / total_excelente
    elif avaliacao == 3:
        cliente += 1
        total_bom += 1
        
    elif avaliacao == 2:
        cliente += 1
    elif avaliacao == 1:
        cliente += 1
        total_pessimo += 1
    else:
        print("Avaliação inválida. Digite um número entre 1 e 4.")
porcentagem_bom = (total_bom / cliente) * 100
print(f"A média da idade dos clientes que avaliaram como excelente é: {media_idade:.0f}")
print("O total de clientes que avaliaram como péssimo é: ", total_pessimo)
print(f"A porcentagem de clientes que avaliaram como bom é: {porcentagem_bom:.1f}%")