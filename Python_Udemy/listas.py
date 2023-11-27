# Listas
# Armazenar mais de uma informacao em variaveis
# Manter a sequencia ddos dados em uma variavel

# Exemplo-1
cidade1 = 'Rio de Janeiro'
cidade2 = 'Sao Paulo'
cidade3 = 'Minas'

# Exemplo-2
cidades = ['Rio de Janeiro', 'Sao Paulo', 'Salvador', 'Goiana']

# indices          0               1           2        3
'''
# imprimindo valor do indece 1
print(cidades)
print(cidades[0])
print(cidades[3])


# Trocando o valor do indece

cidades[0] = 'Brasilia'
print(cidades)

# Adidicionar itens
cidades.append('Santa Catarina')
print(cidades)

# Remover itens
cidades.remove('Salvador')
print(cidades)

# Inserir itens
cidades.insert(1, 'Santa Cataria')
print(cidades)

# Retirar itens
cidades.pop(0)
print(cidades)
# Sort itens # Organiza em ordem alfabetica
cidades.pop()
print(cidades)
'''

# Agregando duas listas com o Zip
# Ou seja o indice-1 da 1 lista
# Junto com o indice-1 da 2 lista

cores = ['Verde', 'Amarelo', 'Azul', 'Branco']
valores = [10, 20, 30, 40,]

duaslistas = zip(cores, valores)


print(list(duaslistas))
