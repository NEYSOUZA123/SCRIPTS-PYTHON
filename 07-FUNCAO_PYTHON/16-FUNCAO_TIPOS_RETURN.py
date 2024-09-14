# Mais sobre o Retun
# -----------------------------------------------------------------------------------------
def minha_soma(n1, n2, n3, n4):
    return n1 + n2 + n3 + n4


print(minha_soma(1, 2, 3, 4))


# -------------------------------------------------------------------------------------------
def bateu_meta(vendas, meta):
    if vendas >= meta:
        return True
    else:
        return False


vendasjose = 60
meta = 55

bateu_meta(vendasjose, meta)
if vendasjose > meta:
    print('Jose bateu a meta')
else:
    print('jose nao bateu a meta')


# ------------------------------------------------------------------------------------------


def padroniza_texto(texto):
    texto = texto.casefold()
    texto = texto.replace('', '')
    texto = texto.upper()
    texto = texto.strip()
    return texto


digitando = input('digite um texto')

texto_padronizado = padroniza_texto(digitando)
print(texto_padronizado)


# ----------------------------------------------------------------------------------------------------

def filtra_lista_texto(lista, pedaco_texto):
    lista_filtrada = []
    for item in lista:
        if pedaco_texto in item:
            lista_filtrada.append(item)
    return lista_filtrada


lista_texto = ['lira@gmail.com', 'souzaclaudiney87@gmail.com', 'welligton@gmail.com', 'carlos@gmial.com',
               'tome@hotmail.com']
listando = filtra_lista_texto(lista_texto, 'gmail')
print(listando)

# ---------------------------------------------------------------------------------------------------------


