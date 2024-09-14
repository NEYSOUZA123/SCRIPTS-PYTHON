# Transformando Listas em Dicionario e Fuction zip

### Estrutura:

# - Dicionário com valores padrões:

# dicionario = dict.fromkeys(lista_chaves, valor_padrao)

# - Dicionário a partir de listas de tuplas:

# dicionario = dict(lista_tuplas)

# - Dicionário a partir de 2 listas:

# Passo 1: Transformar listas em lista de tuplas com o método zip<br>
# Passo 2: Transformar em dicionario

# lista_tuplas = zip(lista1, lista2)<br>
# dicionario = dict(lista_tuplas)

produtos = ['iphone', 'samsung galaxy', 'tv samsung', 'ps5', 'tablet', 'ipad', 'tv philco', 'notebook hp',
            'notebook dell', 'notebook asus']
vendas = [15000, 12000, 10000, 14300, 1720, 1000, 2500, 1000, 17000, 2450]

lista_tuplas = zip(produtos, vendas)#empacintado duas Listas

dicionario = dict(lista_tuplas)

chaves = dicionario.keys()
qtd = dicionario.values()

print(chaves)
print(qtd)

for chaves, qtd in dicionario.items():
    print('produto {} quantidade {}'.format(chaves, qtd))

indice = produtos.index('ipad')
print('Vendedemos {} ipad'.format(vendas[indice]))



#----------------------------------------------------------------------------------------------------------------#

produtos = ['iphone', 'samsung galaxy', 'tv samsung', 'ps5', 'tablet', 'ipad', 'tv philco', 'notebook hp',
            'notebook dell', 'notebook asus']
vendas2019 = [15000, 12000, 10000, 14300, 1720, 1000, 2500, 1000, 17000, 2450]
vendas2020 = [150, 120, 100, 1430, 170, 100, 250, 100, 1700, 250]

vendas_juntar = list(zip(vendas2019, vendas2020))

lista_vendas = dict(vendas_juntar)


produto = list(zip(produtos,vendas_juntar))

lista_completa = dict(produto)

print(lista_completa)

