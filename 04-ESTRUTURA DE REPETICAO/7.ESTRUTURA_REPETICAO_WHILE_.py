# Estrutura While


# Usamos While quando queremos repetir um codigo de forma inderteminada ate a condicao se torna verdadeira/falsa
venda = []
while True:

    opcao = input('Deseja registrar um Produto: S/N')

    if opcao == 'S':
        produto = input("Registre um Produto")
        venda.append(produto)
    elif opcao == 'N':
        print('Registro de produto cadastrado foram {}'.format(venda))
        break
    else:
        print('Opcao Invalida digite a Opcao Correta')
