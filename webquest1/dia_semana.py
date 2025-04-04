#Curso: Licenciatura Ciência da Computação
#Disciplina: Programação 1
#1° Webquest TITULO: Explorando a Programação: Programando Soluções para o Dia a Dia   
#Aluna: Karine Viana Caldas da Silva

# Dicionário com os dias da semana
dias_da_semana = {
    1: "Domingo",
    2: "Segunda-feira",
    3: "Terça-feira",
    4: "Quarta-feira",
    5: "Quinta-feira",
    6: "Sexta-feira",
    7: "Sábado"
}

#Entrada de Dados
dia = int(input("Digite um número entre 1 e 7: "))

#Processamento e Saída de Dados
if dia in dias_da_semana:
    print(f"Hoje é {dias_da_semana[dia]}!")
else:
    print("Digite uma opção válida!")
    