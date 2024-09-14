#exercicio

produtos = ['geladeira', 'sofa', 'fogao']
estoque = [10, 5, 3]

digitar = input('Produto:')



if digitar in produtos:  # verifica se tem na lista de produtos in
    i = produtos.index(digitar)
    qtd_estoque = estoque[i]
    print('A quantide em estoque do produto {} e de {} unidade'.format(digitar,qtd_estoque))

else:
    print("Produto nao existe no estoque")

