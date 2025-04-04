#Curso: Licenciatura Ciência da Computação
#Disciplina: Programação 1
#1° Webquest TITULO: Explorando a Programação: Programando Soluções para o Dia a Dia   
#Aluna: Karine Viana Caldas da Silva

# Variáveis
idade = 0
MESES = 12
DIAS = 365
resultado_mes = 0
resultado_dia = 0

# Entrada de Dados
idade = int(input("Digite a sua idade: "))

# Processamento de Dados 
# Cálculo para conversão de idade "ano" para quantidade de meses de vida
resultado_mes = idade * MESES

# Cálculo para conversão de idade "ano" para quantidade de dias de vida
resultado_dia = idade * DIAS

# Saída de Dados
print(f"""
Você viveu {resultado_mes} meses
E viveu {resultado_dia} dias
""")
