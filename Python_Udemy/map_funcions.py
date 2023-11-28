# Function Filter
# Filtra o resultado dentro de uma lista
# Aplica uma funcao a um Itarable, filtrando os items.
# (list, tuple, dic etc.)

valores = [10, 12, 34, 44, 57]


def remover20(x):
    return x > 20


# Aqui list convert map dentro de remover20 em valores
print(list(map(remover20, valores)))
# Aqui list convert filter dentro de remover20 em valores
print(list(filter(remover20, valores)))

# Aqui usando lambda para reduzir a funcition inteira
print(list(filter(lambda x: x > 40, valores)))
