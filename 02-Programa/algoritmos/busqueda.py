def busqueda_lineal(lista, valor, key=lambda x: x):
    for i, item in enumerate(lista):
        if key(item) == valor:
            return i, item
    return -1, None


def busqueda_binaria(lista, valor, key=lambda x: x):
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        val_medio = key(lista[medio])
        if val_medio == valor:
            return medio, lista[medio]
        elif val_medio < valor:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1, None
