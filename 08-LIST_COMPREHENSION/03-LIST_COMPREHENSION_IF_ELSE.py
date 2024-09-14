# LIST COMPREHENSION COM CONDICAO

produtos_acima_da_meta = []

meta = 1000

vendas_produto = [1500, 150, 200, 1950]

produtos = ['vinho', 'cafeteira', 'microondas', 'iphone']

produtos_acima_da_meta_2 = [produtos for i, produtos in enumerate(produtos) if vendas_produto[i] > meta]
produtos_acima_da_meta_qtd = [vendas_produto for i, vendas_produto in enumerate(vendas_produto) if
                              vendas_produto > meta]
print(produtos_acima_da_meta_2)
print(produtos_acima_da_meta_qtd)

