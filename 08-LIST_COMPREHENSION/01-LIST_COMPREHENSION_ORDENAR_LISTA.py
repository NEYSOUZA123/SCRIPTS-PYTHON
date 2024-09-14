venda_produto = [1500, 150, 210, 1950]

produto = ['vinho', 'cafeteira', 'microondas', 'iphone']

lista_aux = list(zip(venda_produto, produto))
lista_aux.sort(reverse=True)
produto = [produto for vendas, produto in lista_aux]  # List COMPREHENSION
print(produto)

