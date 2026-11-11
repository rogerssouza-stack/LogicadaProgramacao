alunos = 0
total_notas = 0
notas7 = 0
qtdNotas = 0
mediaTurma = 0

while alunos < 35:
    nome = str(input("Digite o nome do aluno: "))
    nota = float(input("Digite a nota do aluno: "))

    total_notas += nota
    if nota > 7:
        notas7 += 1
        
    alunos += 1
    qtdNotas += 1

mediaTurma = total_notas / qtdNotas

print(f"A média geral da turma é: {mediaTurma:.2f}")
print("A quantidade de alunos com nota acima de 7 é: ", notas7)