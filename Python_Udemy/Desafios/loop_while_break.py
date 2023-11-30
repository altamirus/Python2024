# Usando loop com While com break
# Para quando aparecer o 5
# Usar o continue quando visualizar o 5


print('Loop com Break')
for numero in range(1, 11):
    if numero > 5:
        break
    print(numero)


print('Loop com continue:')
for numero in range(1, 11):
    if numero == 5:  # Pula o numero 5
        continue
    print(numero)
