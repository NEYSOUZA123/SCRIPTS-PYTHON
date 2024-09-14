#ESTRUTURA

# O ENUMERATE PERMITE QUE VOCE PERCORRA UMA LISTA E AO MESMO TEMPO TENHA EM UMA VARIAVEL
# O INDICE DAQUELE ITEM

funcionarios = ['maria','Jose','Antonio','JOAO','FRANCISCO','ANA','LUIZ']

for funcionario in funcionarios:
    funcionario = funcionario.upper()
    print(funcionario)

# USANDO ENUMERATE

for i , funcionario in enumerate(funcionarios):
    print('{} e o funcionario {}'.format(i,funcionario))



