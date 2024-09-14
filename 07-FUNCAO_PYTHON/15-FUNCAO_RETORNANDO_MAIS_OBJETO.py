# Como "retornar" mais de um objeto
# É possível retornar 2 "coisas"? 2 listas, 2 strings, 2 números...
# - Sim, basta retornar como uma tupla com 2 itens (vamos fazer um exemplo)

def Operacao_basicas(num1, num2):
    soma = num1 + num2
    multiplica = num1 * num2
    divisao = num1 / num2
    return soma, multiplica, divisao


print(Operacao_basicas(10, 2))
