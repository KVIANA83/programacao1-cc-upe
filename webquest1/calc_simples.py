#Curso: Licenciatura Ciência da Computação
#Disciplina: Programação 1
#1° Webquest TITULO: Explorando a Programação: Programando Soluções para o Dia a Dia   
#Aluna: Karine Viana Caldas da Silva

# Variáveis
numero1 = 0
numero2 = 0
operacao = 0
resultado = 0

# Entrada de Dados 
numero1 = int(input("Digite um número inteiro: "))
numero2 = int(input("Digite outro número inteiro: "))

# Informativo para escolha do usuário
print("""
Escolha o tipo de operação: 
1- Soma
2- Subtração
3- Multiplicação
4- Divisão
""")

operacao = int(input("Digite uma opção: "))

# Processamento e Saída dos Dados
if operacao == 1: 
    resultado = numero1 + numero2
    print(f"O resultado é: {resultado}")

elif operacao == 2: 
    resultado = numero1 - numero2
    print(f"O resultado é: {resultado}")

elif operacao == 3: 
    resultado = numero1 * numero2
    print(f"O resultado é: {resultado}")

elif operacao == 4: 
    resultado = numero1 / numero2
    print(f"O resultado é: {resultado}")

else: 
    print("Digite uma opção valida!")