vendas = [1500, 300, 900, 1000, 2000, 154, 9000, 1254, 20, 30, 90, 80, 40, 50]

meta = 1000

quantidade_bateu = 0

quantidade_nao_bateu = 0

for venda in vendas:
    if venda >= meta:
        print(venda)
        quantidade_bateu += 1
    elif venda <= meta:
        print(venda)
        quantidade_nao_bateu += 1

qtd_funcionarios = len(vendas)
print(quantidade_bateu)
print(quantidade_nao_bateu)
print(qtd_funcionarios)

print("O percentual de funcionarios que bateu a meta e {:.0%}".format(quantidade_bateu / qtd_funcionarios))
print("O percentual de funcionarios que não bateu a meta e {:.0%}".format(quantidade_nao_bateu / qtd_funcionarios))

