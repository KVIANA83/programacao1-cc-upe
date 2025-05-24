# 15. Verificar quantos alunos foram aprovados

aprovados = 0
for i in range(5):
    nota = float(input(f"Nota do aluno {i+1}: "))
    if nota >= 7:
        aprovados += 1
print("Total de alunos aprovados:", aprovados)

