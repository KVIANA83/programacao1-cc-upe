# 16. Divisíveis por 2, 3 e 5
d2 = d3 = d5 = 0
while True:
    n = int(input("Digite um número (0 para sair): "))
    if n == 0:
        break
    if n % 2 == 0:
        d2 += 1
    if n % 3 == 0:
        d3 += 1
    if n % 5 == 0:
        d5 += 1
print("Divisíveis por 2:", d2, "por 3:", d3, "por 5:", d5)