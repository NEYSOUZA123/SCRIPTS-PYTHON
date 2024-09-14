def padronizar_padrao(lista_codigos, padrao='m'):
    for i, item in enumerate(lista_codigos):
        item = item.replace(' ', ' ')
        item = item.strip()
        if padrao == 'm':
            item = item.casefold()
        elif padrao == 'M':
            item = item.upper()
        lista_codigos[i] = item
    return lista_codigos


cod_produto = ['ABC12', 'abc34', 'Abc37']
print(padronizar_padrao(cod_produto, 'M'))
