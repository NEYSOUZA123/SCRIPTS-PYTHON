# ESTRUTURA

# O FOR NO PYTHON CONSEGUE PERCORRER UMA LISTA E A CADA "LOOP" RETORNA O VALOR DO ITEM.


produtos = ['gasolina', 'diesil', 'alcool', 'etanol', 'Gas glp']

for produtos in produtos:  # PARA CADA ITEM DA MINHA LISTA PRODUTO PERCORRER CADA ITEM
    produtos = produtos.upper()#DEIXA A LETRA FORMATO MAIUSCULA
    print(produtos)

# exemplo 2

nome = 'souzaclaudiney87@gmail.com'


for ch in nome:
    ch = ch.upper()#DEIXA A LETRA FORMATO MAIUSCULA
    print(ch)


