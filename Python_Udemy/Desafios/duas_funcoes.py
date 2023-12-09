#

def dobrar(num):
    return num * 2


def quadrado(num):
    return dobrar(num) ** 2


user_num = int(input('Digite um numero: '))
print(f'O quadrado do dobro do numero {user_num} e {quadrado(user_num)}')
