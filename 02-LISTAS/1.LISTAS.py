#Listas em Python

produto = ['guarana','leite','tomate','carne']
quantidade = [12,20,50,30]
vendas = [1500,50,90,30]


print(produto[1])#indice da lista
print(produto)

print('vendas do produto {} foram de {} unidades'.format(produto[0],vendas[0]))#Relacionando Listas

#Modificar o Valor das Listas

vendas[0]=300
produto[0]= 'sabonete'
print('vendas do produto {} foram de {} unidades'.format(produto[0],vendas[0]))#Relacionando Listas

