# Dictionary ( dicionarios)
# Utiliza index no formato de keys e values (Chave e Valor)
# aceita strings, interger, float, boolean

aluno = {'nome': 'Ana', 'idade': '16', 'nota': '10', 'aprovado': 'True'}

# Exemplos 1 loop default com variavel (Mostra apenas os valores)
print('##################')
for x in aluno.values():
    print(x)

print('##################')

# Exemplos 1 loop default com variavel (Mostra apenas as chaves)
for keys in aluno.keys():
    print(keys)

print('##################')

# Ex; 2 loop com Items(Mostra todos os itens)
for items in aluno.items():

    print(items)
print('#######################')
