estoque = [1200, 3000, 90, 55, 70]

produto = ['pepsi 350 ml', 'skol 330 ml', 'brahma 350 ml', 'coca-cola 350 ml', 'itaiva 350ml']

nivel_minimo = 100

for i, qtd in enumerate(estoque):
    if qtd < nivel_minimo:
        print('O produto {}, esta abaixo do nivel minimo temos apenas {} unidades em estoque'.format(produto[i],qtd))
