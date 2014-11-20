import sys


# si es con 2 piezas la hice!, iterando nomas, pero no se me ocurrio como encontrar mas piezas posibles

def pos(personas):
    if personas == []:
        return ['']
    lista = []
    for i in range(len(personas)):
        for j in pos(personas[:i] + personas[i + 1:]):
            lista.append(personas[i] + ',' + j)
    return lista


def posibles(personas, piezas):
    lista = [i.split(',') for i in [j[:-1] for j in pos(personas)]]
    piezas_posibles = []
    for i in piezas:
        for j in lista:
            if (sorted(j[:i]), sorted(j[i:])) not in piezas_posibles:
                piezas_posibles.append((sorted(j[:i]), sorted(j[i:])))
    return piezas_posibles


def validos(personas, piezas, odios):
    piezas_posibles = posibles(personas, piezas)
    l = 0
    for i, j in odios:
        for m in piezas_posibles:
            for n in m:
                if i in n and j in n:
                    l += 1
    if l / (len(piezas)) < len(piezas_posibles):
        return True
    return False


entrada = sys.stdin.readline().strip().split(' ')

piezas = int(entrada[0])
personas = int(entrada[1])
odios = int(entrada[2])

listapiezas = []
listapersonas = []
listaodios = []

i = 0
while i < piezas:
    capacidad = sys.stdin.readline().strip()
    listapiezas.append(int(capacidad))
    i += 1

i = 0
while i < personas:
    persona = sys.stdin.readline().strip()
    listapersonas.append(persona)
    i += 1

i = 0
while i < odios:
    odio = sys.stdin.readline().strip().split(' ')
    listaodios.append(tuple(sorted(odio)))
    i += 1

print(validos(listapersonas, listapiezas, listaodios))
