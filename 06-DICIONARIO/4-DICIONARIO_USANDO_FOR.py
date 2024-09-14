
# estrutura

vendas_tecnologia = {'iphone': 1500, 'sansung galaxy': 1200, 'ps5': 14300, ' sansung tablet': 1720,'lg tablet':500}


for chave in vendas_tecnologia:
    print(chave)
    print('{}: {} unidades'.format(chave, vendas_tecnologia[chave]))


#Qual o total do notebooks vendidos

total_produto_sansung = 0
for chave in vendas_tecnologia:
    if 'sansung' in chave:
        total_produto_sansung = total_produto_sansung + vendas_tecnologia[chave]
        print(total_produto_sansung)
