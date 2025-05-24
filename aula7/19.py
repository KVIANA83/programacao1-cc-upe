# 19. Média entre 50 e 100
soma = 0
cont = 0
while True:
    n = int(input("Digite um número (0 para sair): "))
    if n == 0:
        break
    if 50 <= n <= 100:
        soma += n
        cont += 1
if cont > 0:
    print("Média entre 50 e 100:", soma / cont)
else:
    print("Nenhum número no intervalo.")