
# Desafios com 'SETs'

'''
Criar um programa que gera 3 listas de acordo com a necessidade logo abaixo:

Lista = funcionarios que tem carro e trabalha a noite
Lista = funcionarios que tem carro e trabalha de dia
Lista = funcionario que nao tem carro

'''
funcionarios = ['Ana', 'Marcos', 'Alice',
                'Pedro', 'Sophia', 'Bruno', 'Melissa',]
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa',]
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa',]


tc = set(tem_carro).intersection(turno_noite)
print(tc)
td = set(tem_carro).intersection(turno_dia)
print(td)
tn = set(funcionarios).difference(tem_carro)
print(tn)
