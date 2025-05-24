# 20. Menor valor positivo e ímpar
menor = None
while True:
    n = int(input("Digite um número (0 para sair): "))
    if n == 0:
        break
    if n > 0 and n % 2 == 1:
        if menor is None or n < menor:
            menor = n
if menor is not None:
    print("Menor valor positivo e ímpar:", menor)
else:
    print("Nenhum valor positivo e ímpar digitado.")