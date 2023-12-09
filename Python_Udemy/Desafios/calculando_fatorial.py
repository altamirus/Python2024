# Funcoes recursivas

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)


usernumber = int(input('Digite um numero:'))
print(f'O Fatorial de {usernumber} e {fatorial(usernumber)}')
