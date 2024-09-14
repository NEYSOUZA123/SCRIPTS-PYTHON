

# Adicionar, Remover e Modificar itens no Dicionario

# dicionario = {}

# dicionario[chave] = valor

# outra opçao:

# dicionario.update({chave:valor,chave:valor})

lucro_1tri = {'janeiro': 1000, 'fevereiro': 12000, 'marco': 9000}

lucro_2tri = {'abril': 8800, 'maio': 12000, 'junho': 500}

# Juntando dois dicionarios com o metodo update

lucro_1tri.update(lucro_2tri)

print(lucro_1tri)

# Modificando o valor de uma chave  no dicionario

lucro_1tri['janeiro'] = 8800,
lucro_2tri['abri'] = 5

print(lucro_1tri)

# removendo um chave do dicionario

del lucro_1tri['junho']

print(lucro_1tri)

# Guardado a Lista caso queira armazenar

lucro_junho = lucro_1tri.pop('fevereiro')
print(lucro_junho)

