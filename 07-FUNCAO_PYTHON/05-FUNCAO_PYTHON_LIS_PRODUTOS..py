# O custo da lata é 80/18 = 4,44 R\\$/L

# O custo do galão é 25/3,6 = 6,94 R\\$/L

# A lata é mais econômica, então todas as latas inteiras que pudermos usar devemos comprar em latas. Se ficar faltando alguma coisa para completar devemos avaliar se é melhor comprar latas ou galões. Exemplo:

# Se queremos comprar 90 litros. 5 latas dão exatamente 90 litros. Então devemos comprar tudo em latas.

# Se queremos comprar 95 litros. 5 latas dão exatamente 90 litros. Então devemos comprar pelo menos 5 latas e avaliar
# o que falta, se estes últimos 5 litros valem mais apenas em latas ou galões.

# Para os 5 litros faltantes precisamos de 2 galões que custam 50 reais no total. Ou de uma lata que custa 80 reais
# no total. Portanto, neste caso vale mais a pena usar 2 galões.

# Se queremos comprar 107 litros. 5 latas dão exatamente 90 litros. Então devemos comprar pelo menos 5 latas e
# avaliar o que falta, se estes últimos 5 litros valem mais apenas em latas ou galões.

# Para os 17 litros faltantes precisamos de 5 galões que custam 125 reais no total. Ou de uma lata que custa 80 reais
# no total. Portanto, neste caso vale mais a pena usar uma lata.

# 3 galões custam 75 reais, 4 galões custam 100 reais. Então, se for possível completar com até 3 galões escolhe-se
# galões. Qualquer quantidade maior que 3 galões, usa-se latas.

# Podemos ir ao exercício:


# PEGAR AREA A SER PINTADA
def area_a_ser_pintada():
    area = int(input('DIGITE A AREA A SER PINTADA EM M²: '))
    return area


def calcular_litros_tinta(area):
    litros = area / 6
    return litros


def calcula_qtd_galoes_latas(litros):
    lata_inteira = int(litros // 18)
    litros_faltam = litros % 18

    # Se for preencher com latas
    custo_extra_lata = 80

    # Se for preencher com galões
    galoes = litros_faltam / 3.6
    if galoes > int(galoes):
        galoes = int(galoes) + 1
    custo_extra_galoes = galoes * 25

    if custo_extra_lata < custo_extra_galoes:
        latas = lata_inteira + 1
        galoes = 0
    else:
        latas = lata_inteira
        galoes = int(galoes)

    return latas, galoes


def calcular_custo(latas,galoes):
    custo_latas = latas * 80
    custo_galoes = galoes * 25
    custo = custo_latas + custo_galoes
    return custo


# Executa o programa
area = area_a_ser_pintada()
litros = calcular_litros_tinta(area)
latas, galoes = calcula_qtd_galoes_latas(litros)
custo = calcular_custo(latas, galoes)

print("Litros necessários:", litros)
print("Quantidade de latas:", latas)
print("Quantidade de galões:", galoes)
print("Custo total:", custo)
