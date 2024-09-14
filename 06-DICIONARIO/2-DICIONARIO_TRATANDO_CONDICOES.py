mais_vendido = {'tecnologia': 'iphone', 'refrigeracao': 'Ar consul 1200 btu', 'livros': 'o Alquimista'}

vendas_tecnologia = {'iphone': 1500, 'sasung galaxy': 1200, 'ps5': 14300, 'tablet': 1720}

# respondendo com a chave , igua a aula anterior

print('O livro mais vendido foi o {}'.format(mais_vendido['livros']))

# respondedo pelo metodo get

print(vendas_tecnologia.get('iphone'))
print('Vendemos {} tablet'.format(vendas_tecnologia.get('tablet')))

# -------------------------------------------------------------------------------------#

# Usando o if


if 'iphone' in vendas_tecnologia:
    print('Temos em estoque do produto iphone {}'.format(vendas_tecnologia['iphone']))
else:
    print('O produto nao esta armazenado no seu estoque')

# --------------------------------------------------------------------------------------#

# Outra forma de tratar a condicao

if vendas_tecnologia.get('ps5') == None:
    print('O produto nao esta armazenado no seu estoque')
else:
    print(vendas_tecnologia.get('ps5'))

