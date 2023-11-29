# Dry - Don't repeat yourself
# Funcions (Funcoes)
#
# Varios argumentos (xargs) identificando o paametro
# Criar uma funcao que armazena numeros e strings (dados)

def agencia(**carro):
    return carro


print(agencia(marca='Gol', cor='Branca', motor='1.0'))
print(agencia(marca='Fiat', cor='Cinza', motor='1234'))
print(agencia(marca='Byd', cor='Preto', placa='4321'))
