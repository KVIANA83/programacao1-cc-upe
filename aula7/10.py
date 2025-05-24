# 10. Soma dos cubos dos dígitos
n = int(input("Digite um número: "))
soma = 0
while n > 0:
    digito = n % 10
    soma += digito**3
    n //= 10
print("Soma dos cubos dos dígitos:", soma)