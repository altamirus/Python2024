# Sets
# Listas e varias opcoes de verificar itens duplicados
# nao utiliza index (perde a indexacao)
# 1-union ('|') Uniao duas ou mais listas
# 2-diference ('-') Diferenca entre dois ou mais listas
# 3-simetric ('^') Symetric Difference
# -And ('&') And

'''cores1 = ['Verde', 'Amarelo', 'Azul', 'Branco', 'Roxo']
cores2 = ['Vermelho', 'Amarelo', 'Azul', 'Branco']
listas1 = [10, 20, 25, 40,]
listas2 = [10, 22, 27, 40,]

num1 = set(listas1)
num2 = set(listas2)
cor1 = set(cores1)
cor2 = set(cores2)

print(num1 | num2)
print(num1 - num2)
print(num1 ^ num2)
print(num1 & num2)
print(cor1 & cor2)
print(cor1 | cor2)
print(cor1 ^ cor2)
print(cor1 - cor2)
'''


# Funcoes em sets
# funcao - add (Adiciona um item)
# funcao - update (Atualiza um iten)
# funcao - remove (Gera erro se o objeto nao existir)
# funcao - discard (Nao Gera erro se o objeto nao existir)


s1 = {1, 2, 3, 4, 5, 6}
s1.add(6)
s1.update([6, 7, 8, 9, 10])
s1.remove(10)
s1.discard(90)

print(s1)
