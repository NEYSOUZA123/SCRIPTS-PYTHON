vendas = ('Lira', 'carlos', 'luiz', 30, 20, 11)

nome1, nome2, nome3, idade1, idade2, idade3 = vendas

print(nome3)

# O enumarate que vinhamos usando ate agora , na verdade cria uma tupla para a gente. Vamos ver na pratica

venda = [
    ('20/08/2020', 'iphone x', 'azul', '128gb', 350, 4000),
    ('20/08/2020', 'iphone x', 'prata', '128gb', 1500, 4000),
    ('20/08/2020', 'ipad', 'prata', '256gb', 127, 6000),
    ('20/08/2020', 'ipad', 'prata', '128gb', 981, 5000),
    ('21/08/2020', 'iphone x', 'azul', '128gb', 397, 4000),
    ('21/08/2020', 'iphone x', 'prata', '128gb', 1017, 4000),
    ('21/08/2020', 'ipad', 'prata', '256gb', 50, 6000),
    ('21/08/2020', 'ipad', 'prata', '128gb', 4000, 5000),
]
faturamento = 0

produto_mais_vendido = ''
quantidade_mais_vendida = 0
cor_mais_vendida = ''

for item in venda:
    data, produto, cor, capacidade, quantidade, valor = item
    if produto == 'iphone x' and data == '20/08/2020':
        faturamento += quantidade * valor
print('O faturamento na data 20/08/2020 de iphone  foi de {} '.format(faturamento))
for item in venda:
    data, produto, cor, capacidade, quantidade, valor = item
    if data == '21/08/2020':
        if quantidade > quantidade_mais_vendida:
            produto_mais_vendido = produto
            quantidade_mais_vendida = quantidade
            cor_mais_vendida = cor
print('Meu produto mais vendido foi o {} da cor {} no dia {}, com a quantidade de {}'.format(produto_mais_vendido,cor,data,quantidade))
