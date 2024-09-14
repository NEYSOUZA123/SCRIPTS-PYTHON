produto = []


def Cadastrar_produto():
    produto = input('Digite o produto para Cadastro')
    produto = produto.upper()
    print('O produto {} foi cadasttrado com Sucesso!'.format(produto))


for i in range(5):
    Cadastrar_produto()
