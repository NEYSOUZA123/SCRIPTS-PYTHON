# Programa para ler credeciais do ususario

usuario = 'ney'

senha = 540

while True:
    digita_usuario = input('Digite o Usuario ')
    if digita_usuario != usuario:
        print('Usuario Invalido digite Usuario correto')
        continue

    digitar_senha = int(input('Digite a senha do usuario'))
    if digitar_senha != senha:
        print('Senha invalidade')
    else:
        print('Seja Bem Vindo ao Programa')
        break

    # -----------------------------Menu Interarivo--------------------------------------------
clientes = []

while True:
    print('\nMenu:')
    print('1. Cadastrar um Cliente')
    print('2. Listar Clientes')
    print('3. Sair')

    opcao = int(input('Escolha a Opcao:'))

    if opcao == 1:
        cadastro_cliente = input('Nome do Cliente:')
        clientes.append(cadastro_cliente)
    elif opcao == 2:
        if not clientes:
            print('Nenhum Cliente Cadastrado')
        else:
            print('Clientes Cadastrados')
            for cliente in clientes:
                print(cliente)
    elif opcao == 3:
        print('Saindo do Programa')
        break
