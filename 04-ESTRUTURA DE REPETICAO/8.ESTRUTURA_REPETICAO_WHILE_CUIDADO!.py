# Cuidado com While > Loop infinito

# Sempre que for usar while Lembre-se de ter certeza que o programa vai terminar em algum momento

vendas = [941, 852, 65, 65, 64, 804, 20]

vendedores = ['maria', 'jose', 'lima', 'tome', 'Carlos', 'Adriano', 'Luiz']

meta = 50

i = 0

while vendas[i] > meta:
    print('{} bateu a meta. Vendas {}'.format(vendedores[i], vendas[i]))
    break  # Nesse caso Tratamos com o Break para interromper o codigo infinito.


while vendas[i] > meta:
    print('{} bateu a meta. Vendas {}'.format(vendedores[i], vendas[i]))
    i = i+1



