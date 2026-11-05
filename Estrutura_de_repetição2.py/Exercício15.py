pop1 = int(input("Insira a população do país A (milhões): "))
pop2 = int(input("Insira a população do país B (milhões): "))
ano = 0
while pop2 > pop1:
    pop1 *= 1.035
    pop2 *= 1.01
    ano += 1
print("A quantidade de anos necessários para o país A ultrapassar o país o país B serão: ", ano)