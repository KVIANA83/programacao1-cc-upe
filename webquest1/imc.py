#Curso: Licenciatura Ciência da Computação
#Disciplina: Programação 1
#1° Webquest TITULO: Explorando a Programação: Programando Soluções para o Dia a Dia   
#Aluna: Karine Viana Caldas da Silva

# IMC = peso / (altura * altura)
# Tabela 
# IMC - Classificação
# Menor que 18,5 - Magreza
# 18,5 a 24,5 - Normal
# 25 a 29,9 - Sobrepeso
# 30 a 34,9 - Obesidade grau 1
# 35 a 39,9 - Obesidade grau 2
# Maior que 40 - Obesidade grau 3

# Variáveis
peso = 0
altura = 0
imc = 0

# Entrada de Dados 
peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite sua altura (em cm): "))

# Processamento e Saída de Dados
imc = peso / (altura * altura)

if imc >= 18.5 or imc <= 24.5: 
    print(f"seu peso é {imc}, classificação: Normal")

elif imc < 18.5 or imc >= 0:
    print(f"seu peso é {imc}, classificação: Magreza")
        
elif imc >= 25 or imc <= 29.9:
    print(f"seu peso é {imc}, classificação: Sobrepeso")
    
elif imc >= 30 or imc <= 34.9:
    print(f"seu peso é {imc}, classificação: Obesidade grau 1")
    
elif imc >= 35 or imc <= 39.9:
    print(f"seu peso é {imc}, classificação: Obesidade grau 2")
    
elif imc >= 40:
    print(f"seu peso é {imc}, classificação: Obesidade grau 3")
    
else: 
    print("Digite um valor válido!")    
