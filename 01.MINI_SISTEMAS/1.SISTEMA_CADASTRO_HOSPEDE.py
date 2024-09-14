#SISTEMA DE SERIÇO DE HOSPEDE


quantidade_hospede = int(input("DIGITE A QUANTIDADE DE HOSPEDE NO QUARTO :"))
quarto = []

for i in range(quantidade_hospede):
    while True:
        nome = input("Nome:")
        if nome == "":
           print('O nome não pode conter campos vazios , por favor preenchar os campos')
           continue

        cpf = input("CPF")
        if cpf == "":
            print('CPF NÃO PODE CONTER CAMPOS VAZIO, DIGITE NOVAMENTE')
            continue
        hospede = [nome, 'cpf:{}'.format(cpf)]
        quarto.append(hospede)
        break

    print(quarto)
