
# 8. Maior e menor número
maior = None
menor = None
while True:
    n = int(input("Digite um número (0 para sair): "))
    if n == 0:
        break
    if maior is None or n > maior:
        maior = n
    if menor is None or n < menor:
        menor = n
print("Maior:", maior)
print("Menor:", menor)