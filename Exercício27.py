funcionarios = 0
total_pagos = 0
total_admin = 0
total_operacional = 0
count_admin = 0
count_operacional = 0

while funcionarios < 20:
    cod = int(input("Digite o código do funcionário: "))
    salario = float(input("Digite o salário do funcionário: "))
    total_pagos += salario

    if cod == 1:
        total_admin += salario
        count_admin += 1
    elif cod == 2:
        total_operacional += salario
        count_operacional += 1

    funcionarios += 1

if count_admin > 0:
    media_admin = total_admin / count_admin
else:
    media_admin = 0

if count_operacional > 0:
    media_operacional = total_operacional / count_operacional
else:
    media_operacional = 0

print(f"Total de salários pagos pela empresa: R${total_pagos:.2f}")
print(f"Quantidade de funcionários no setor administrativo: {count_admin}")
print(f"Quantidade de funcionários no setor operacional: {count_operacional}")
print(f"Média salarial do setor administrativo: R${media_admin:.2f}")
print(f"Média salarial do setor operacional: R${media_operacional:.2f}")