# 18. Números com mais de trás dígitos
cont = 0
while True:
    n = int(input("Digite um número (0 para sair): "))
    if n == 0:
        break
    if abs(n) > 999:
        cont += 1
print("Números com mais de 3 dígitos:", cont)