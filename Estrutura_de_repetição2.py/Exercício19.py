cliente = 0
while cliente < 150:
    nome = str(input("Escreva seu nome: "))
    valor = int(input("Insira o valor das compras no ano passado: "))
    if valor < 500000:
        valorFinal = valor * 0.90
        cliente += 1
    else:
        valorFinal = valor * 0.85
        cliente += 1
print(nome, "de acordo com suas compras do ano passado você recebeu um bônus de 10% do valor destas compras se o valor foi menor que 500000 e 15% se foi maior que 500000 o que deixa você com um valor de ", valorFinal)