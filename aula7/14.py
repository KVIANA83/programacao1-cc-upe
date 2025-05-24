# 14. Pares antes do primeiro ímpar
pares = 0
while True:
    n = int(input("Digite um número (0 para sair): "))
    if n == 0 or n % 2 != 0:
        break
    pares += 1
print("Pares antes do primeiro ímpar:", pares)