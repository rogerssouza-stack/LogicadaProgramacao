valorCarro = float(input("Insira o valor do carro: "))
parcelas = int(input("Insira a quantidade de parcelas: "))
precoFinal = 0
valorParcela = 0
match parcelas:
    case 0:
        precoFinal = valorCarro * 0.80
        valorParcela = precoFinal
    case 6: 
        precoFinal = valorCarro * 1.03  
        valorParcela = precoFinal / 6
    case 12: 
        precoFinal = valorCarro * 1.06 
        valorParcela = precoFinal / 12
    case 18: 
        precoFinal = valorCarro * 1.09 
        valorParcela = precoFinal / 18
    case 24: 
        precoFinal = valorCarro * 1.12 
        valorParcela = precoFinal / 24
    case 30: 
        precoFinal = valorCarro * 1.15 
        valorParcela = precoFinal / 30
    case 36: 
        precoFinal = valorCarro * 1.18 
        valorParcela = precoFinal / 36
    case 42: 
        precoFinal = valorCarro * 1.21 
        valorParcela = precoFinal / 42
    case 48: 
        precoFinal = valorCarro * 1.24 
        valorParcela = precoFinal / 48
    case 54:
        precoFinal = valorCarro * 1.27 
        valorParcela = precoFinal / 54
    case 60: 
        precoFinal = valorCarro * 1.30 
        valorParcela = precoFinal / 60

print("A quantidade de parcelas é ", parcelas, "sendo que o carro ficou com o valor final de ", precoFinal, " com cada parcela custando ", valorParcela)