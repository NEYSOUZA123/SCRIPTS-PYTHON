# --------------------ESTRUTURA DE REPETICAO---------------------------------------------#

for i in range(3):  # i e a contagem de referencia
    print(i)
# ----------------------------------------------------------------------------------------#


print("-----------------------------------------------------------------------------------")


produtos = ['arroz', 'acuca', 'sal', 'carne']
producao = [150, 30, 70, 90]

cadastra_produto = input("CADASTRE O PRODUTO DESEJADO: ")

cadastra_estoque = int(input("ESTOQUE DO PRODUTO: "))


produtos.append(cadastra_produto)
producao.append(cadastra_estoque)

for n in range(len(produtos)):
    print('{} unidade produzida de {}'.format(producao[n], produtos[n]))


