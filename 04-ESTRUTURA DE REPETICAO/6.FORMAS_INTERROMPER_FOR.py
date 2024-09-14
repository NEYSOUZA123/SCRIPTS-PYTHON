# 2 Opcoes:

# . break > Iterrompe e finaliza o for
# continue > interrompe e vai para o proximo item o for


vendas = [130, 1500, 2000, 200, 50, 60]

meta = 130

for venda in vendas:
    if venda < meta:
        continue
    print(venda)  # continue pula para o proximo item do for
