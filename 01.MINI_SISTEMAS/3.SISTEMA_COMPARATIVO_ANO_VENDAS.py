produtos = ['iphone','computador','nootbok','maquina de cafe','geladeira']

vendas2019 = [150,90,60,30,80]
vendas2020 = [30,95,180,32,87]

for i , produtos in enumerate(produtos):
    if vendas2020[i]>vendas2019[i]:
        crescimento = vendas2020[i]/vendas2019[i]-1
        print('O  produto {} no ano de 2020  vendeu a quantidade de {} e em 2019 vendeu {} , teve um crescimento de {:.1%}'.format(produtos,vendas2020[i],vendas2019[i],crescimento))

