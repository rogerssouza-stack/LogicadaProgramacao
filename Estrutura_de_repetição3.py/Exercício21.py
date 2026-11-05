pessoas = 0
homens = 0
mulheres = 0
while pessoas < 56:
    nome = str(input("Escreva seu nome: "))
    sexo = str(input("Escreva seu sexo: "))
    if sexo == "masculino":
        print("A pessoa de nome ", nome, "tem o sexo definido como masculino.")
        pessoas += 1
        homens += 1
    else:
        print("A pessoa de nome ", nome, "tem o sexo definido como feminino.")
        pessoas += 1
        mulheres += 1
print("O número total de homens é", homens, "Enquanto o número total de mulheres é de", mulheres)