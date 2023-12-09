# Lembre-se a diferenca entre 'Tuple' e 'List'!!!
# List = pode ser alterado os itens
# Tuple = nao pode ser alterado os itens

cidades = ('Sao Paulo', 'Teresina', 'Rio de Janeiro')

busca_cidade = input('Digite o nome da Cidade: ')
if busca_cidade in cidades:
    print(f'A Cidade de {busca_cidade} esta na lista')
else:
    print(f'A Cidade de {busca_cidade} nao esta na lista')
