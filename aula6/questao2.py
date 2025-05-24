# Crie um array vazio chamado "numeros"
# a. adicione os numeros 1,2,3 e 4 ao array
# b. acesse o valor do segundo elemento do array
# c. atualize o valor do terceiro elemento do array para 10
# d. remova o último elemento do array utilizando a função ".pop"
# e. verifique o comprimento do array

# 2. Manipulação de array "numeros"

numeros = []

numeros.extend([1, 2, 3, 4])  # a
print("Segundo elemento:", numeros[1])  # b
numeros[2] = 10  # c
numeros.pop()  # d
print("Comprimento do array:", len(numeros))  # e

