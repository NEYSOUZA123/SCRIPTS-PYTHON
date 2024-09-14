meta = 10000

vendas = [
    ['joa', 15000],
    ['lira', 5],
    ['marcus', 990],
    ['maria', 16000],
    ['ana', 10300],
]

for item in vendas:
    if item[1] > meta:
        print(' O VENDEDOR {} BATEU A META FEZ {} VENDAS'.format(item[0].upper(), item[1]))

    elif item[1] < meta:
        print(' O VENDEDOR {} NÃO BATEU A META FEZ {} VENDAS'.format(item[0].upper(), item[1]))

