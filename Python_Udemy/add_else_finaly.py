# Try Except com input
#
'''try:
    valor = int(input('Digite o valor do Produto: '))
    print(type(valor))
except ValueError:
    print('Favor digite um numero')
else:
    print('Usuario digitou um valor correto')
    resultado = valor * 2
    print(resultado)

print('Mais resultado aqui')'''

# usando finaly
try:
    valor = int(input('Digite o valor do Produto: '))
    print(type(valor))
except ValueError:
    print('Favor digite um numero')
finally:
    print('Usuario digitou um valor correto')
    resultado = valor * 2
    print(resultado)

print('Codigo ok')
