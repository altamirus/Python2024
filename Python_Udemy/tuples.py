# Tuples
# Armazenas mais de uma informacao em variaveis
# Manter a sequencia dos dados em uma variavel
# Nao podem ser alteradas (Immutable)


cores_tuples = ('Verde', 'Amarelo', 'Azul', 'Branco')
cores_list = ['Verde', 'Amarelo', 'Azul', 'Branco']


print(cores_tuples)
print(type(cores_list))
print(type(cores_tuples))

duas_listas = cores_list * 2
duas_tuples = cores_tuples * 2
print(duas_listas)
print(duas_tuples)

cores_list.append('Roxo')
print(cores_list)

# List sim e possivel inserir, remover, modificar(+ memori - agilidade)
# Tuples nao e possivel inserir, remover, modificar (+ rapdo - memoria)
# Gera um erro -->cores_tuples.append('roxo')
