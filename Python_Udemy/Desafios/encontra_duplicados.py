# Lembrando que SETs sao especificos para buscar
# verificar quais itens estao em comun entre dois ou mais SETs
#

amigos1 = {'Altamiro', 'Miriam', 'Drielly', 'Amanda'}
amigos2 = {'Silva', 'Bia', 'Drielly', 'Amanda'}

result = amigos1.intersection(amigos2)
# result = amigos1.union(amigos2)
# result = amigos1.difference(amigos2)

print(result)
