# PROGRAMA QUE CONTROLA O ESTOQUE

estoque = [88, 39, 50, 90]

produto = ['arroz', 'acuca', 'leite', 'nescal', ]

estoque_minimo = 44

for i in range(len(estoque)):
    if estoque[i] >= estoque_minimo:
        print('O produto {} esta acima de estoque minimo'.format(produto[i]))

for i in range(len(estoque)):
    if estoque[i] <= estoque_minimo:
        print("O produto {} esta abaixo do estoque minimo".format(produto[i]))
