#Comparadores

# igual e ==
# diferente !=
# > maior que ( >= maior ou igual)
# < menor que ( <= menor ou igual)
# texto existe dentro de outro texto comando  in
# Verifica ao contrario da comparação    not

faturamentoLoja1 = 2500
faturamentoLoja2 = 2200

if faturamentoLoja1 == faturamentoLoja2:
    print("Faturamento da Loja são iguais")
else:
    print("O faturamento da loja e diferente")


print("Programa 2")

email = "Lira@gmail.com"

#---------------------------------- Acesso ao email----------------------------------------------------
emaildigitar = input("Digite o email:")

if emaildigitar == email:
    print("Email correto Seja bem vindo")
else:
    print("Email incorreto digite o email correto")

#========================================================================================================

print("Programa 03")
emailusuario = input("Insira o email do usuario")
if not '@' in emailusuario:
    print("Email Invalido")
else:
    print("Email valido")
    pass

