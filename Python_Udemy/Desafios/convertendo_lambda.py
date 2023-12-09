# Para este desafio, crie uma funcao lambsa
# que aceire um numro e retorne o cubo desse numero.

# forma convencional
# def cubo(num):
#     return num ** 3

# Usando funcao Lambda
def cubo(num): return num ** 3


user_number = int(input(f'Digite um numero: '))

print(f'O cubo de {user_number} e {cubo(user_number)}')
