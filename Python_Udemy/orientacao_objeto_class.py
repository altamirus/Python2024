# Python Object-Oriented Programming
# classes
# utilizadas para criar objetos(instances)
# Objetos sao partes dentro de uma class (instancias)
# classes sao utilizadas para agrupar dados e funcoes, podendo reutilizar

# Criando uma class

class Funcionarios:
    pass


# criando o objeto
usuario1 = Funcionarios()
usuario2 = Funcionarios()

# criando os parametros do usuario1
usuario1.nome = 'Altamiro'
usuario1.sobrenome = 'Pereira'
usuario1.data_nascimento = '07/05/1979'
print(usuario1.nome)


# criando os parametros do usuario2
usuario2.nome = 'Altamirando'
usuario2.sobrenome = 'Pereira'
usuario2.data_nascimento = '07/05/1979'
print(usuario2.nome)
