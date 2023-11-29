from datetime import datetime
# Python Object-Oriented Programming
# Construtores-classes
# utilizadas para criar objetos(instances)
# Objetos sao partes dentro de uma class (instancias)
# classes sao utilizadas para agrupar dados e funcoes, podendo reutilizar


class Funcionarios:
    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome

    def idade_funcionario(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento

    # Todo constructor deve usar __init__ parainiciar
    # Deve usar self


# criando o objeto
usuario1 = Funcionarios('Altamiro', 'Pereira', 1978)
usuario2 = Funcionarios('Altamirando', 'Pereira', 1979)
usuario3 = Funcionarios('Miriam', 'Pereira', 1980)


print(Funcionarios.idade_funcionario(usuario1))
print(Funcionarios.nome_completo(usuario2))
print(Funcionarios.idade_funcionario(usuario3))

# criando os parametros do usuario1
# usuario1.nome = 'Altamiro'
# usuario1.sobrenome = 'Pereira'
# usuario1.data_nascimento = '07/05/1979'


# # criando os parametros do usuario2
# usuario2.nome = 'Altamirando'
# usuario2.sobrenome = 'Pereira'
# usuario2.data_nascimento = '07/05/1979'
