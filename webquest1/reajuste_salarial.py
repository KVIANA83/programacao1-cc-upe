#Curso: Licenciatura Ciência da Computação
#Disciplina: Programação 1
#1° Webquest TITULO: Explorando a Programação: Programando Soluções para o Dia a Dia   
#Aluna: Karine Viana Caldas da Silva

#Variavéis
salario = 0
aumento1 = 0
aumento2 = 0
percentual1 = 0
percentual2 = 0

#Processamento e Saída de Dados
salario = float(input("Digite o valor do seu salário: R$ "))

percentual1 = salario/100 * 10
aumento1 = salario + percentual1

percentual2 = salario/100 *15
aumento2 = salario + percentual2

if salario == 1500:
    
    print(f"""
    O valor de aumento é de 10% R$ {percentual1:.2f}
    Seu novo salário é R$ {aumento1:.2f}   
        """)
elif salario > 1500:
    print(f"""
    O valor de aumento é de 10% R$ {percentual1:.2f}
    Seu novo salário é R$ {aumento1:.2f}
    """)
else: 
    print(f"""
    O valor de aumento é de 15% R$ {percentual2:.2f}
    Seu novo salário é R$ {aumento2:.2f}
    """)