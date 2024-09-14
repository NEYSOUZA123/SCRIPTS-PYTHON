    #Sistema para loja de Tinta em Geral 

def area_ser_pintada():
    area = int(input("Digite o valor da area a ser pintada"))
    return area


def calcular_litros_tintas(area):
    litros = area / 65
    return litros

def calcular_latas_tintas(litros):
    latas = litros / 3.06
    if latas > int(latas):
        latas = int(latas) + 1
    return latas

def calcula_custo(latas):
    custo = latas * 80
    return custo




area = area_ser_pintada()
litro = calcular_litros_tintas(area)
latas = calcular_latas_tintas(litro)
custo = calcula_custo(latas)


print("latas",latas)
print("custo",custo)