# Comparativo de vendas com o ano anterior


vendas_produtos = [('iphone', 558147, 951642), ('galaxy', 712350, 244295), ('ipad', 573823, 26964),
                   ('tv', 405252, 787604),
                   ('máquina de café', 718654, 867660), ('kindle', 531580, 78830), ('geladeira', 973139, 710331),
                   ('adega', 892292, 646016), ('notebook dell', 422760, 694913), ('notebook hp', 154753, 539704),
                   ('notebook asus', 887061, 324831), ('microsoft surface', 438508, 667179), ('webcam', 237467, 295633)
    , ('caixa de som', 489705, 725316), ('microfone', 328311, 644622), ('câmera canon', 591120, 994303)]

produto_maior_venda = ''

ano_maior2019 = 0

ano_maior2020 = 0

for item in vendas_produtos:
    produto, ano2019, ano2020 = item
    if produto and ano2020 > ano2019:
        ano_maior2019 = ano2019
        ano_maior2020 = ano2020
        produto_maior_venda = produto
        acrescimo = ano_maior2020 / ano_maior2019-1
        soma = ano_maior2020-ano_maior2019
        print('O produto {} teve um aumento de vendas em {:.1%} no ano de 2020 uma diferenca de {} unidades vendidasX'.format(produto_maior_venda,acrescimo,soma))


