# VAMOS CRIAR UM PROGRAMA PARA ANALISAR O BONUS DOS FUNCIONARIOS


meta_vendas = float(input("DIGITE A META DE VENDA:"))

vendas = float(input("TOTAL DE VENDAS:"))


if   vendas < meta_vendas:
     print("Não ganhou Bonus")
elif vendas > (meta_vendas*2):#*Se dobrou a meta
     bonus = 0.07 * vendas
     print('Ganhou {:.2f} de bonus'.format(bonus))
else:
    bonus = 0.03 * vendas
    print("Ganhou {:.2f} de bonus".format(bonus))



