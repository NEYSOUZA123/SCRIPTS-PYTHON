produtos = ['arroz', 'açuca', 'cafe', 'leite']
vendas = [50,30,90,500]

# -------------------------------Tamanho da Lista------------------------------------------------
tamanho = len(produtos)#verifica o tamanho da Lista

print(tamanho)

# ------------------------------------------------------------------------------------------------

# ----------------------------Maior e Menor Valor de uma lista-------------------------------------

maior_valor = max(produtos)
meno_valor = min(produtos)

print(maior_valor)
print(meno_valor)

maior_valor_vendas = max(vendas)
menor_vlaor_vendas = min(vendas)


print('O produto como o Maior valor de vendas foi {} e o menor foi {}'.format(maior_valor_vendas,menor_vlaor_vendas))

i = vendas.index(maior_valor_vendas)
i = vendas.index(menor_vlaor_vendas)
produto_mais_vendido = produtos[i]
produto_menos_vendido = produtos[i]
print('O produto com o menor valor de vendas e o {} com vendas de {} unidade e o maior e o {} com vendas de {} unidades'.format(produto_menos_vendido,menor_vlaor_vendas,produto_mais_vendido,maior_valor_vendas))

