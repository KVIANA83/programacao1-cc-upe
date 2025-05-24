# 1. Criando dicionário vazio e verificando o tipo
objeto = {}
print("Tipo de 'objeto':", type(objeto))

# 2. Criando dicionário 'pessoa' com propriedades
pessoa = {"nome": "Maria", "idade": 30, "endereço": "Rua das Flores, 123"}

# 3. Acessando valor da propriedade 'nome'
print("Nome:", pessoa["nome"])

# 4. Adicionando nova propriedade 'profissao'
pessoa["profissao"] = "Engenheira"

# 5. Atualizando a idade
pessoa["idade"] = 35
print("Pessoa atualizada:", pessoa)

# 6. Criando dicionário 'animal'
animal = {"nome": "Rex", "especie": "Cachorro", "cor": "Marrom"}
print("Animal:", animal)

# 7. Criando dicionário 'livro'
livro = {"titulo": "O Pequeno Príncipe", "autor": "Antoine de Saint-Exupéry", "ano": 1943}

# 8. Acessando valor do autor
print("Autor do livro:", livro["autor"])

# 9. Atualizando o ano do livro
livro["ano"] = 2000

# 10. Excluindo a propriedade 'titulo'
del livro["titulo"]
print("Livro após exclusão:", livro)

# 11. Criando dicionário 'carro' e exibindo
carro = {"marca": "Toyota", "modelo": "Corolla", "ano": 2020}
print("Carro:", carro)

# 12. Atualizando modelo para None
carro["modelo"] = None
print("Carro atualizado:", carro)

# 13. Criando dicionário 'aluno' e lista 'alunos'
aluno = {"nome": "João", "idade": 20}
alunos = [aluno]

# a. Acessando nome do primeiro aluno
print("Nome do primeiro aluno:", alunos[0]["nome"])

# b. Adicionando mais 3 alunos
alunos.append({"nome": "Ana", "idade": 21})
alunos.append({"nome": "Carlos", "idade": 22})
alunos.append({"nome": "Beatriz", "idade": 23})
print("Lista de alunos:", alunos)
