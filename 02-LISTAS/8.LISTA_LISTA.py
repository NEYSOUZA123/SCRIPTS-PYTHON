# Lista de Lista

# Estruturas

vendores = ['joao', 'Marcos', 'Pedro', 'Caio']

produtos = ['ipad', 'iphone']

vendas = [[200, 50],
          [50, 90],
          [150, 30],
          [60, 85],
          [30, 55],
          ]
vendas_ipad_joao = vendas[1][0]

print(vendas_ipad_joao)

vendas_iphone_Pedro = vendas[2][1]

print(vendas_iphone_Pedro)

total_vendas_iphone = vendas[0][1] + vendas[1][1] + vendas[2][1] + vendas[3][1] + vendas[4][1]

print('O total de vendas do Produto {} e de {}'.format(produtos[1], total_vendas_iphone))

# e se o Lira fez apenas 50 vendas de iphone

vendas[4][1] = 50
print(vendas)

# e se agora eu tenho um novo produto 'mac'

vendas_mac = [12,56,35,77,88]

vendas[0].append(vendas_mac[0])
vendas[1].append(vendas_mac[1])
vendas[2].append(vendas_mac[2])
vendas[3].append(vendas_mac[3])
vendas[4].append(vendas_mac[4])


print(vendas)
