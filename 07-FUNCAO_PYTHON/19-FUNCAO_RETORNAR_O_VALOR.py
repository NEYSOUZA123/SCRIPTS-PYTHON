# Retornar um valor na Function python

# Estrutura basica

# def nome_funcao ():
# return valor_final

def cadastrar_produto():
    produto = input('Digite o produto para cadastro')
    produto = produto.casefold()
    print('O produto {} foi cadastrado com sucesso'.format(produto))
    return produto


variavel_produto = cadastrar_produto()
print(variavel_produto)

