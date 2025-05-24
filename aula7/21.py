# 21. Pares e ímpares entre o primeiro e último
numeros = []
while True:
    n = int(input("Digite um número (0 para sair): "))
    if n == 0:
        break
    numeros.append(n)
if len(numeros) >= 2:
    inicio = numeros[0]
    fim = numeros[-1]
    pares = impares = 0
    for i in range(min(inicio, fim), max(inicio, fim) + 1):
        if i % 2 == 0:
            pares += 1
        else:
            impares += 1
    print("Pares:", pares, "ímpares:", impares)
else:
    print("Não foi possível calcular.")