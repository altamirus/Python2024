# O que sao erros
# Trabalhando com Try Except com listas

'''#Aqui erro nao tratado
letras = ['a', 'b', 'c']
# indices  0    1    2
print(letras[3])
# Gera um erro pois index nao existe (IndexError)
print()
print('########################')
print()'''


'''# Aqui tratamos os erros com 'Try Except'
try:
    letras = ['a', 'b', 'c']
    # indices  0    1    2
    print(letras[3])  # <--Indice 3 nao existe
except IndexError:
    print('###### Index nao Existe ###')
    # Aqui mostra um erro tratado com (IndexError)
    # Mais limpo e amigavel'''


# Try Except com input
#
try:
    valor = int(input('Digite o valor do Produto: '))
    print(type(valor))
except ValueError:
    print('Favor digite um numero')
    print('Continua o programa ainda')
