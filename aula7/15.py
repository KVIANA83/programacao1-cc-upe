# 15. Contar pares e ímpares
pares = 0
impares = 0
while True:
    n = int(input("Digite um número (0 para sair): "))
    if n == 0:
        break
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1
print("Pares:", pares, "Ímpares:", impares)