# List Comprehension
# Mais simples de se escrever
# Utilizado quando voce precisa criar
# uma nova lista a partir de uma existente
# [expressao for iten in itens]

frutas1 = ['abacate', 'banana', 'morango', 'kiwi,', 'abacaxi']
frutas2 = []

# Pesquisando se existe letra C na lista 1 e jogando na lista2
for item in frutas1:
    if 'c' in item:
        frutas2.append(item)
print(frutas2)
print()
print('########################')
print()
# Fazendo o mesmo com apenas uma linha de codigo
# Pesquisando com a letra N
frutas2 = [item for item in frutas1 if 'n' in item]
print(frutas2)
