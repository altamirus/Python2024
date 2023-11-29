# Desafio com funcoes

'''
Criar um programa que caulcula a quantidade de tinta necessaria para 
pintar uma parede. O usuario devera fornecer as seguintes informacoes:
Rendimento, altura e largura.
O programa deve mostrar na tela a mensagem 
'Voce necessita de x latas de tinta'
'''

rendimento = int(input('Digete o rendimento:'))
altura = int(input('Digete altura do muro:'))
largura = int(input('Digete largura do muro:'))


def calculo():
    area = altura * largura
    resultado = area / rendimento
    print(f'Voce precisa de {resultado} latas de tinta ')


calculo()
