# Sistema de Leitura de Numeros


caixa = []

while True:
    opcao = input('Deseja digitar uma nota digite s/ sim ou  n/ não ')
    if opcao == 's':
        nota = int(input("Digite uma nota de 0 a 10"))
        if nota == 0:
            print('Nota Invalida')
            continue
        caixa.append(nota)
    elif opcao == 'n':
        print(caixa)
        break
    else:
        print('Opcao invalida digite uma nota correta')

