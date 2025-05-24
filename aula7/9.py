# 9. Média de números digitados
soma = 0
contador = 0
while True:
    n = int(input("Digite um número (-1 para sair): "))
    if n == -1:
        break
    soma += n
    contador += 1
if contador > 0:
    print("MÃ©dia:", soma / contador)
else:
    print("Nenhum número digitado.")