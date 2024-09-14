#Como Descobrir um Indice Dentro da Lista

produto = ['geladeira','tv','sofa','fogao','teclado','forno']
estoque = [50,30,10,70,20,40]

#Descobrir a Quantidade de estoque produto Geladeira

i = produto.index('sofa')
print(i)
print(produto[i])

qtd_estoque = estoque[i]

print(qtd_estoque)

print('Quantidade e estoque do produto geladeira e de {}'.format(qtd_estoque))

