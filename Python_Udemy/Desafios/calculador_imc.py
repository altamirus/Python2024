# Caulculo de IMC - Indece de Massa Corporal

'''
Qual e a sua Altura em cm:
Qual e o seu peso em kg:

'''

# Meno que 18,5         Magreza
# entre 18,5 e 24,9     Normal
# Entre 25,0 e 29,9     Sobrepso
# Entre 30,0 e 39,0     Obesidade
# Maior que 40,0        Obsedade Morbida

altura = float(input('Qual e sua Altura em cm?:'))
peso = float(input('Qual e seo Peso em kg?:'))
imc = peso / (altura/100)**2

if imc < 18.5:
    print('Magreza')
elif imc >= 18.5 and imc < 24.9:
    print('Normal')
elif imc >= 25.0 and imc < 29.9:
    print('Sobrepeso')
elif imc >= 30.0 and imc < 39.0:
    print('Obesidade')
elif imc > 40.0:
    print('Obsedade Morbida')
