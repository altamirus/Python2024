
numero = [1, 2, 3, 4, 5, 6]


def quadrado(num): return num ** 2


result = []

for i in numero:
    result.append(quadrado(i))

print(f' Os quadrados dos numeros {numero}  são: {result}')
