# 17. Média dos divisíveis por 3
soma = 0
cont = 0
while True:
    n = int(input("Digite um número (0 para sair): "))
    if n == 0:
        break
    if n % 3 == 0:
        soma += n
        cont += 1
if cont > 0:
    print("Média dos divisíveis por 3:", soma / cont)
else:
    print("Nenhum número divisível por 3.")