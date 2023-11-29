
# while loop
# Ideal para loops dependentes de uma condicao.
# Publicar um produto com comissao de 10% se for acima de R$20

valor = int(input('Dgite valor do Produto: '))

while valor >= 20:
    valor = (valor * 0.10) + valor
    print(f' O valor do Produto R${valor}')
    break
