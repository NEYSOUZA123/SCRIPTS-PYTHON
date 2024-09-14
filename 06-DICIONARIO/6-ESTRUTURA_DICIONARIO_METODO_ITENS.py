
vendas_tecnologia = {'nootbook asus': 2450, 'iphone aple': 15000, 'sansung galaxy': 300, 'tv sansung': 50}

for itens, qtd in vendas_tecnologia.items():
    if qtd > 2000 and itens in 'iphone aple ':
        print('{},{} unidades'.format(itens, qtd))

    