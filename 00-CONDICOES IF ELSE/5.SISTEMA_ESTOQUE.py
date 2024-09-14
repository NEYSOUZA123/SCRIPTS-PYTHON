
# MINI SISTEMA CONTROLE DE ESTOQUE HASTG COMPARADORES

while True:
    produto = input('Produto:')
    categoria = input('Categoria:')
    quantidade = input('Quantidade')

    if produto and categoria and quantidade:
        quantidade = int(quantidade)
        if categoria == 'bebidas':
            if quantidade < 75:
                print('Solicitar {} a equipe de compras , temos {} unidades em estoque'.format(produto, quantidade))
            break
        elif categoria == 'limpeza':
            if quantidade < 30:
                print('Solicitar {} a equipe de compras , temos {} unidades em estoque'.format(produto, quantidade))
            break
        elif categoria == 'alimentos':
            if quantidade < 50:
                print('Solicitar {} a equipe de compras , temos {} unidades em estoque'.format(produto, quantidade))
            break
        elif categoria != 'bebidas' != 'limpeza' != 'alimentos':
            print('Categoria incorreta digite a categoria correta')
    else:
        print('Preencha todos os campos')

