
from sys import getsizeof
# Generator Expressions
# Uma forma mais rapda para listas, dicionario e etc
# Valores em bytes


# Teste para virificar quanto de
# memoria isso esta consumindo na memoria
#

# Usando type para saber qual tipagem usada
numeros = [x * 10 for x in range(100)]
print(type(numeros))
print(numeros)
print(getsizeof(numeros))


# Importando 'getsizeof' from 'sys'
# Para saber o tamanho em bytes
# Aqui para transformar em generator basta trocar
# [colchetes] por (parenteses). Observe
numeros = (x * 10 for x in range(100))
print(type(numeros))
print(list(numeros))
print(getsizeof(numeros))


# Observe os valores em bytes(memoria)
# e veja como generator expressions e economize meria.
