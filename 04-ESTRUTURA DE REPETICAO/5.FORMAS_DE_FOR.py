produtos = ['coca-cola', 'fanta', 'pepsi', 'guarana']

precos = [10.50, 3.50, 6.50, 2.80]

# FOR ITEM IN LISTA para percorrer uma Lista

for preco in precos:
    print(preco * 1.1)
print("-------------------------------------------------------------------")
# For i in range usando o for para percorrer duas listas

for i in range(len(precos)):
    produto = produtos[i]
    preco = precos[i]
    print(produto, preco)
print("-------------------------------------------------------------------")
# For item in Lista com enumerate

for i, preco in enumerate(precos):
    preco = preco * 1.1
    produto = produtos[i]
    print(produto,preco)



