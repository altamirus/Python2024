# Dry - Don't repeat yourself
# Funcions (Funcoes)

'''
def boas_vindas():

    print('Ola Altamiro')
    print('Temos 5 laptops em estoque')


boas_vindas()


def somar():
    num1 = 10
    num2 = 5
    resultado = num1 + num2
    print(resultado)


somar()

# Parametros e Argumentos


def ola(nome, qtd):
    print(f' Ola {nome}')
    print(f' Temos {qtd} laptops em estoque')


ola('Marcos', 5)
ola('Maria', 10)
ola('Miriam', 3)

'''

# Default = Aquele que voce define o valor no parametro
# non-Default = Aquele que voce nao define o valor no parametro


def welcome(nome='Miriam', qtd=6):
    print(f' Ola {nome}')
    print(f' Temos {qtd} laptops em estoque')


welcome('Altamiro', 5)
