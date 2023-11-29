# Dictionary ( dicionarios)
# Utiliza index no formato de keys e values (Chave e Valor)
# aceita strings, interger, float, boolean

aluno = {'nome': 'Ana', 'idade': '16', 'nota': '10', 'aprovado': 'True'}

# Atualizando dicionario
aluno.update({'nome': 'Joao', 'nota': '8'})
# Acrescentando Endereco
aluno.update({'endereco': 'Rua 0'})

# Imprimindo na tela para testar
print(aluno)
# Usando metodo get para nao gerar erro com CEP que nao existe
print(aluno.get('cep', 'Nao existe'))
print()
print()
# Divisao na tela para Diferenciar 1 do 2
print('########################')
print()
print()
print()
# Acrescentando o CEP
aluno.update({'cep': '64000000'})
# Imprimindo na tela com CEP atualizado
print(aluno)
