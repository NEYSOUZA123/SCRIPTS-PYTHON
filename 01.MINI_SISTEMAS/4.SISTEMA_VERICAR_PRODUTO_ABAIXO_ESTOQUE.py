estoque = [[294, 60, 565, 50, 64, 20, 30, 68, 97, 8056, 454, 560, 45, 454, 554, 5, 8, 2, 88, 5564, 87, 4, 544, 455],
           [294, 60, 545, 50, 64, 20, 30, 68, 97, 8056, 454, 580, 45, 494, 554, 8, 8, 2, 88, 5564, 87, 4, 54, 455],
           [294, 60, 55, 50, 64, 300, 355, 68, 97, 8056, 454, 560, 69, 454, 554, 900, 80, 200, 88, 5564, 87, 59, 54,
            455],
           [294, 60, 55, 50, 64, 20, 30, 68, 9, 8056, 454, 560, 45, 454, 554, 7, 8, 2, 88, 5564, 87, 4, 544, 455],
           [294, 60, 585, 50, 64, 20, 30, 68, 97, 86, 454, 560, 45, 454, 555, 5, 8, 2, 88, 5564, 87, 4, 54, 45],
           ]
fabrica = ['Hastg treinamento', 'Fabrica Hastg', 'Python Producao', 'Manufatura', 'Treinaweb']

nivel_minimo = 50

fabrica_abaixo_nivel = []

for i, lista in enumerate(estoque):
    for qtd in lista:
        if qtd < nivel_minimo:
            if fabrica[i] in fabrica_abaixo_nivel:
                pass
            else:
                fabrica_abaixo_nivel.append(fabrica[i])

print(fabrica_abaixo_nivel)
