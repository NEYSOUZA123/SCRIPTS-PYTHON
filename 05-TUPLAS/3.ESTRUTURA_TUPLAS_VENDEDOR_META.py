# Analises de vendas metas

meta = 10000
vendas = [
    ('João', 15000),
    ('Julia', 27000),
    ('Marcus', 9900),
    ('Maria', 3750),
    ('Ana', 10300),
    ('Alon', 7870),
]

vendedor_maior_venda = ''

maior_venda = 0

for item in vendas:
    nome, quantidade = item
    if quantidade > maior_venda and quantidade >= meta:
        vendedor_maior_venda = nome
        maior_venda = quantidade
print('A maior venda foi do vendedorª {} que bateu a meta com uma quantidade vendida de {} unidades '.format(vendedor_maior_venda,maior_venda))


