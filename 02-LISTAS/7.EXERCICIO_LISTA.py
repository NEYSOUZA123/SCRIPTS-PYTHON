# -------------- Faturamento do pior e maior valor de venda------------------------------------------

meses = ['jan', 'fev', 'marc', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]

vendas_1sem.extend(vendas_2sem)

maior_valor = max(vendas_1sem)
menor_valor = min(vendas_1sem)

maior_mes = max(meses)
menor_mes = min(meses)

i = vendas_1sem.index(maior_valor)
e = vendas_1sem.index(menor_valor)

mes_mais_vendido = meses[i]
mes_menos_vendido = meses[e]

i_menor_valor = vendas_1sem.index(menor_valor)
i_maior_valor = vendas_1sem.index(maior_valor)

print(
    'O mes mais vendido foi o mes de {} com as vendas de {} e o menor mes foi o mes de {} com as vendas no valor de {}'.format(
        mes_mais_vendido, maior_valor, mes_menos_vendido, menor_valor))

print('O melhor mes de vendas foi {} com vendas {}'.format(meses[i_maior_valor], maior_valor))
print('O pior mes de vendas foi {} com vendas {}'.format(meses[i_menor_valor], menor_valor))
# -------------------------------Calculando Faturamento Total-------------------------------------------

fat_total = sum(vendas_1sem)
print('Faturamento total R${:,}'.format(fat_total))

percentual_maior_valor = maior_valor/fat_total

percentual_menor_valor = menor_valor/fat_total

print('O maior valor foi o mes  de {} reperesentou {:.1%}'.format(meses[i],percentual_maior_valor))
print('O menor valor  foi o  mes de {} reperesentou {:.1%}'.format(meses[i],percentual_menor_valor))


#----------------------------Crie uma Lista top 3--------------------------------


estoque = [50,33,90,70]
produto = ['ACUCA','ARROZ','FEIJAO','OLEO']

maior_estoque = max(estoque)
menor_estoque = min(estoque)

i = estoque.index(maior_estoque)
e = estoque.index(menor_estoque)

produto_mais_vendido = produto[i]
produto_menos_vendido = produto[e]

print(produto[i],maior_estoque)
print(produto[e],menor_estoque)

top3 = []

print(estoque)

maior_valor = max(estoque)
top3.append(maior_valor)
print(top3)
estoque.remove(maior_valor)
print(estoque)
maior_valor = max(estoque)
top3.append(maior_valor)
print(top3)

