#Adicionar ou remover item da Lista

produtos = ['apple', 'tv', 'iphone', 'geladeira']
print('Produtos')
# adicionar ou remover iten da lista
produtos.append('iphone 11')
print(produtos)
produtos.remove('iphone')
print(produtos)

# Usa o pop tambem
item_removido = produtos.pop(3)
print('Removemos o {} da lista'.format(item_removido))

# --------------------Se caso o Produto não tiver na Lista--------------------------------------------#


geladeira = ['alho', 'cebola', 'pimentao', 'morango', 'cenora', 'beterraba']

geladeira_remove = input('Remova o produto')

if geladeira_remove in geladeira:
    geladeira.remove(geladeira_remove)
else:
    print('Não existe o produto {} na lista'.format(geladeira_remove))

print(geladeira)

while True:
    adicionandoalimento = input('Deseja Adicionar Alimento digite (s/n) sim ou não')

    if adicionandoalimento == 's':
        geladeira_adicionar = input('Adicionar Alimentos')
        geladeira.append(geladeira_adicionar)
        print('Alimento Adicionado')
    else:
        print('Muito Obrigado')
        break

    print(geladeira)
    