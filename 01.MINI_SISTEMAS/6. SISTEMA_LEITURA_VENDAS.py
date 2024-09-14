# Faça um programa que leia as vendas dos vendedores , mostre a venda de cada vendedor com seu nome e a media de vendas

vendas = [1000, 1500, 1200, 1300]

vendedores = ['fulano', 'ciclano', 'beltrano', 'Lira']

for i in range(len(vendas)):
    print('Vendas:{},vendedor: {}'.format(vendas[i],vendedores[i]))

media = sum(vendas)/len(vendas)
print('media:',media)



