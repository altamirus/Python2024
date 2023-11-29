# Desafio com if, elif, else

'''
Criar um programa que dependendo da temperatura(em celsius) do steak
ele retorna o ponto de cozimento em portugues. o usuario devera fornecer 
temperatura.

Temperaturas - Cozimento
120˚ ou 48˚C - Rare (Selado)
130˚ ou 54˚C - Medium Rare (Ao ponto para mal)
140˚ ou 60˚C - Medium (Ao ponto)
150˚ ou 65˚C - Medium well (Ao ponto para bem)
160˚ ou 71˚C - Well done (Bem passada)
'''
temperatura = int(input('Digete a temperatura:'))
if temperatura < 48:
    print('Assar uma pouco mais)')
if temperatura < 54:
    print('Rare (Selado)')
elif temperatura <= 60:
    print('Medium Rare (Ao ponto para mal)')
elif temperatura <= 65:
    print('Medium (Ao ponto)')
elif temperatura <= 71:
    print('Medium well (Ao ponto para bem)')
elif temperatura > 100:
    print('Well done (Sapecou)')
