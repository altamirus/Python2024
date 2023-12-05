#
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista = list(range(1, 11))
# numero = int(input('Digite um numero: '))
for i in lista:
    if i % 2 == 0:
        print(f'O numero {i} e PAR')
    else:
        print(f'O numero {i} e IMPAR')
