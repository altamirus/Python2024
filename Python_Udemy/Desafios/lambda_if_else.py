#
def par_ou_impar(num):
    if num % 2 == 0:
        return 'Par'
    else:
        return 'Impar'


user_number = int(input('Digite um numero: '))
print(f'O numero {user_number} é {par_ou_impar(user_number)}')
