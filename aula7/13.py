# 13. Aprovados (nota >= 7)
i = 0
aprovados = 0
while i < 5:
    nota = float(input("Digite a nota do aluno: "))
    if nota >= 7:
        aprovados += 1
    i += 1
print("Alunos aprovados:", aprovados)