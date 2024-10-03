lista = [1, 2, 3, 4, 5]

print(lista)
print(*lista)


def suma(a, b):
    return a + b


print(suma(1, 2))


def suma_numere(*numere):
    suma = 0
    for nr in numere:
        suma = suma + nr

    return suma


print(suma_numere(1, 2, 3, 4, 5, 6, 546, 546, 546, 456, 546))
print(suma_numere(1, 2))
print(suma_numere(1, 2, 3, 4))
