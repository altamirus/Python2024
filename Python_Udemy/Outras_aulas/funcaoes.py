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



# Default = Aquele que voce define o valor no parametro
# non-Default = Aquele que voce nao define o valor no parametro


def welcome(nome='Miriam', qtd=6):
    print(f' Ola {nome}')
    print(f' Temos {qtd} laptops em estoque')


welcome('Altamiro', 5)


# Realizar uma tarefa
# Calcular e retorna um valor


def cliente1(nome):
    print(f' Ola {nome}')


def cliente2(nome):
    return f' Ola {nome}'


cliente1('Maria')
print(cliente2('jose'))

print()
print('###################')
print()

x = cliente1('Maria')
y = cliente2('jose')

print(x)
print(y)

'''

# xargs
# Varios argumentos (sargs)

# Criar uma funcao que soma varios numeros.


def soma(*numeros):
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado


x = soma(2, 3, 4, 7, 10)

print(x)
