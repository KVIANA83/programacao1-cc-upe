# 18. Média da altura de 5 pessoas

alturas = []
for i in range(5):
    altura = float(input(f"Digite a altura da pessoa {i+1} (em metros): "))
    alturas.append(altura)
media_altura = sum(alturas) / len(alturas)
print("Média das alturas:", round(media_altura, 2))

