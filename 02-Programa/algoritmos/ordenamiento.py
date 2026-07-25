def burbuja(lista, key=lambda x: x):
    copia = lista[:]
    n = len(copia)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if key(copia[j]) > key(copia[j + 1]):
                copia[j], copia[j + 1] = copia[j + 1], copia[j]
    return copia


def merge_sort(lista, key=lambda x: x):
    if len(lista) <= 1:
        return lista[:]
    medio = len(lista) // 2
    izq = merge_sort(lista[:medio], key)
    der = merge_sort(lista[medio:], key)
    return _merge(izq, der, key)


def _merge(izq, der, key):
    resultado = []
    i = j = 0
    while i < len(izq) and j < len(der):
        if key(izq[i]) <= key(der[j]):
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado
