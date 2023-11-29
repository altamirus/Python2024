# Python Object-Oriented Programming
# Construtores-classes
# utilizadas para criar objetos(instances)
# Objetos sao partes dentro de uma class (instancias)
# classes sao utilizadas para agrupar dados e funcoes, podendo reutilizar

class Funcionarios:
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome

    def nome_completo_date(self):
        return self.nome + ' ' + self.sobrenome + ' ' + self.data_nascimento

    # Todo constructor deve usar __init__ parainiciar
    # Deve usar self


# criando o objeto
usuario1 = Funcionarios('Altamiro', 'Pereira', '07/05/1979')
usuario2 = Funcionarios('Altamirando', 'Pereira', '08/05/1979')


print(usuario1.nome_completo())
print(Funcionarios.nome_completo_date(usuario1))
print(usuario2.nome_completo_date())
print(Funcionarios.nome_completo(usuario2))

# criando os parametros do usuario1
# usuario1.nome = 'Altamiro'
# usuario1.sobrenome = 'Pereira'
# usuario1.data_nascimento = '07/05/1979'


# # criando os parametros do usuario2
# usuario2.nome = 'Altamirando'
# usuario2.sobrenome = 'Pereira'
# usuario2.data_nascimento = '07/05/1979'
