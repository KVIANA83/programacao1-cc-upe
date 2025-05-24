# 13. Maior e menor entre 10 números digitados

valores = []
for i in range(10):
    n = int(input(f"Digite o {i+1}º número: "))
    valores.append(n)
print("Maior valor:", max(valores))
print("Menor valor:", min(valores))

