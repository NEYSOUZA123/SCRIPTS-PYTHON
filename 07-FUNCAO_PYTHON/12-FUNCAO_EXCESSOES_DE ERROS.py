# Exceções e Erros e tratar exceções

# Como "testar" erros e tratar exceções

# try:
# o que eu quero tentar fazer
# except:
# o que vou fazer caso de erro


def descobrir_servidor(email):
    try:
        posicao_a = email.index('@')
    except:
        print('Email digitidado nao tem @ digite novamente')
    else:
        servidor = email[posicao_a:]
        if 'gmail' in servidor:
            return 'gmail'
        elif 'outllok' in servidor or 'live' in servidor:
            return 'hotmail'
        elif 'yahho' in servidor:
            return 'yahho'
        elif 'uol' in servidor:
            return 'uol'
        else:
            return 'nao determinado'


email = input('Digite o email indexado')

print(descobrir_servidor(email))
