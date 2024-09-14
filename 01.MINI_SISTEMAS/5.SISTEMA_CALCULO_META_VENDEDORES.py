meta = 1000

vendas = [
    ['joao', 150],
    ['maria', 1500],
    ['pedro', 800],
    ['carlos', 3000],

]

acima_meta = []

for venda in vendas:
    if venda[1] >= meta:
        acima_meta.append(venda)

print(acima_meta)
print('{:.0%} de vendedores bateram a meta'.format(len(acima_meta) / len(vendas)))

# CALCULO DIRETAMENTE NA lISTA

quantidade_vendedores_acima_meta = 0

for venda in vendas:
    if venda[1] >= meta:
        quantidade_vendedores_acima_meta += 1
if quantidade_vendedores_acima_meta == 1:
    print('Apenas {} vendedor bateu a meta '.format(quantidade_vendedores_acima_meta))
elif quantidade_vendedores_acima_meta > 1:
    print('A quantidade de vendedores que bateram a meta foi de {} vendedores'.format(
        quantidade_vendedores_acima_meta))

#Calculando qual foi o Melhor vendedor


melhor_vendedor = ''

maior_venda = 0

for venda in vendas:
    if venda[1] > maior_venda:
        maior_venda = venda[1]
        melhor_vendedor = venda[0]
print('O Melhor Vendedor foi {}'.format(melhor_vendedor))

