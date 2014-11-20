import sys

ruta = sys.stdin.readline().strip()
a = open(ruta)
lista = a.readlines()
lista1 = []
for i in range(len(lista)):
    aux = lista[i].strip().split()
    lista1.append(aux)

fila = str(len(lista1))
columna = str(len(lista1[0]))


def rowmayor(lista, fila, columna):
    print(fila + ' ' + columna + ' ' + lista[0].strip() + ' ' + lista[1])


def rowmenor(lista):
    string = ""
    for i, j in zip(lista[0], lista[1]):
        string += i + ' ' + j + ' '
    print(str(len(lista)) + ' ' +
          str(len(lista[0])) + ' ' + string.strip())


rowmayor(lista, fila, columna)
rowmenor(lista1)
