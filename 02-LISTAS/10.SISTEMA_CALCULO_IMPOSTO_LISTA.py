produtos = ['computador', 'livro', 'tv', 'geladeira']

produtos_ecomercy = [[1500, 3000],
                     [3300, 600],
                     [7500, 990],
                     [854, 990],
                     ]

if 'livro' in produtos:
    i_livro = produtos.index('livro')
    print(i_livro)
    total_antigo = produtos_ecomercy[i_livro][0] * produtos_ecomercy[i_livro][1]
    print('O total antigo e de R${:.2f}'.format(total_antigo))
    produtos_ecomercy[i_livro][1] = produtos_ecomercy[i_livro][1] * 1.1
    novototal = produtos_ecomercy[i_livro][0] * produtos_ecomercy[i_livro][1]
    print(novototal)
    print(
        'O total antigo era de R${:.2f} com o calculo do imposto passou a ser R${:.2f}'.format(total_antigo, novototal))
    print('Acrescimo do imposto de R${:.2f} mil reais'.format(novototal - total_antigo))
else:
    print('Não existe em estoque o item Livro')


