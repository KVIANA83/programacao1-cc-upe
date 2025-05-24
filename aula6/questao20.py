# 20. Soma dos dígitos pares de um número inteiro

numero = input("Digite um número inteiro: ")
soma_pares = sum(int(digito) for digito in numero if int(digito) % 2 == 0)
print("Soma dos dígitos pares:", soma_pares)

