# 21. Pares e Ã­mpares entre o primeiro e Ãºltimo
numeros = []
while True:
    n = int(input("Digite um nÃºmero (0 para sair): "))
    if n == 0:
        break
    numeros.append(n)
if len(numeros) >= 2:
    inicio = numeros[0]
    fim = numeros[-1]
    pares = impares = 0
    for i in range(min(inicio, fim), max(inicio, fim) + 1):
        if i % 2 == 0:
            pares += 1
        else:
            impares += 1
    print("Pares:", pares, "Ãmpares:", impares)
else:
    print("NÃ£o foi possÃ­vel calcular.")