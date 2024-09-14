# -------------------------------Juntando estoque--------------------------------------------

estoque_antigo = ['cadeira', 'mesa', 'cama']

quantidade_estoque = [55, 40, 30]

estoque_novo = ['tv']

juntar_estoque = estoque_novo + estoque_antigo

print(juntar_estoque)

# --------------------------------------------------------------------------------------------
# ---------------------- Juntando a Lista------------------------------------------------------
juntar_estoque.extend(estoque_antigo)
print(juntar_estoque)

# _____________________________Ordenar Listas_________________________________________________

estoque_antigo.sort()
quantidade_estoque.sort(reverse=True)

print(estoque_antigo)
print(quantidade_estoque)

print('\n'.join(estoque_antigo))  # Printar Lista com o metodo join

produtos = 'geladeira ,tv , sofa , computador , Maquina de Lavar ,Video game '

lista = produtos.split(',')

print(lista)