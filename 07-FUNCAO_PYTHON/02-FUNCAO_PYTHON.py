produto = []

def Cadastrar_Produto():
    item = input('Produto')
    item = item.upper()
    produto.append(item)
    return produto


Cadastrar_Produto()
print(produto)
