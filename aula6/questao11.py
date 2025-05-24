# 11. Média de 5 notas

notas = []
for i in range(5):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas.append(nota)
media = sum(notas) / len(notas)
print("Média das notas:", media)

