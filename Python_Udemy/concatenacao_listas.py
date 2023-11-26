# Listas
# Armazenar mais de uma informacao em variaveis
# Manter a sequencia ddos dados em uma variavel


numeros = [2, 3, 4, 5]
letras = ['a', 'b', 'c', 'd']

por1 = numeros * 1
por2 = numeros * 2
por3 = numeros * 3
porLetras = numeros + letras

print(por1)
print(por2)
print(por3)
print(porLetras)

# Unpacking Lists (Desempacotar listas)

produtos = ['arroz', 'feijao', 'laranja', 'Batata',  5, 6, 7, 8]

item1, item2, *outros, item8 = produtos

print(item1)
print(item2)
print(item8)
print(*outros)
