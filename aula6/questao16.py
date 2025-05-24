# 16. Soma dos dígitos de um número

numero = input("Digite um número inteiro: ")
soma_digitos = sum(int(digito) for digito in numero)
print("Soma dos dígitos:", soma_digitos)

