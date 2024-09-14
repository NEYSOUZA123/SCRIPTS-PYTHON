# Dicionario em Python

# Estrutura

# Vantagens e Desvantagens

# Nao devem ser usados para pegar itens em uma determinada ordem
# Podem ter valores Heterogenios (varios tipo dentro)
# Chaves sao unicas obrigatoriamente
# Mais intuitivo de trabalhar

mais_vendido = {'tecnologia': 'iphone', 'refrigeracao': 'Ar consul 1200 btu', 'livros': 'o Alquimista'}

vendas_tecnologia = {'iphone': 1500, 'sasung galaxy': 1200, 'ps5': 14300, 'tablet': 1720}

# Qual foi o item mais vendido nas categorias 'livros'e 'lazer'?

qtd_PS5 = vendas_tecnologia['ps5']
qtd_sansung = vendas_tecnologia['sasung galaxy']
lazer = mais_vendido['refrigeracao']
qtd_iphone = vendas_tecnologia['iphone']
qtd_tablet = vendas_tecnologia['tablet']



print(qtd_PS5)
print(qtd_sansung)
print(lazer)
print(qtd_iphone)
print(qtd_tablet)


