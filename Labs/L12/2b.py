def pos(personas):
    if personas == []:
        return ['']
    lista = []
    for i in range(len(personas)):
        for j in pos(personas[:i] + personas[i + 1:]):
            lista.append(personas[i] + ',' + j)
    return lista


def posibles(personas, piezas):
    lista=[]
    piezas_posibles = []
    for i in piezas:
        for j in lista:
            if (sorted(j[:i]), sorted(j[i:])) not in piezas_posibles:
                piezas_posibles.append((sorted(j[:i]), sorted(j[i:])))
    return piezas_posibles


def pieza(personas, piezas):
    posibles = [i.split(',') for i in [j[:-1] for j in pos(personas)]]
    l = []
    i = 0
    while i < len(posibles):
        li = []
        orden = posibles[i]
        j = 0
        while j < len(piezas):
            largo = piezas[j]
            li.append(orden[:largo])
            orden = orden[largo:]
            j+=1
        l.append(li)
        i += 1
    for i in l:
        for j in i:
            j.sort()
    l.sort()
    i=0
    while i<len(l):
        j=0
        while j<len(l):
            if l[i]==l[j] and i!=j:
                l.remove(l[j])
                j-=1
            j+=1
        i+=1
    for i in range(len(l)):
        l[i] = tuple(l[i])
    return l


def validos(personas, piezas, odios):
    piezas_posibles = posibles(personas, piezas)
    l = 0
    for i, j in odios:
        for m in piezas_posibles:
            for n in m:
                if i in n and j in n:
                    l+=1
    if l/(len(piezas))<len(piezas_posibles):
        return True
    return False


a = posibles(['a', 'b', 'c', 'd', 'e'], [2, 3])
a = pieza(['pedro', 'jose', 'mario', 'juan'], [2, 3])
b = validos(['pedro', 'jose', 'mario', 'juan'], [2, 3], [('mario', 'pedro'), ('jose', 'pedro'), ('jose', 'juan')])
ba = validos(['pedro', 'jose', 'mario', 'juan', 'ignacio'], [2, 3], [('mario', 'pedro'), ('jose', 'pedro'), ('jose', 'juan'), ('ignacio', 'pedro'), ('ignacio', 'jose')])
c = posibles(['pedro', 'jose', 'mario', 'juan', 'ignacio'], [2, 3])

print(b)


personas = ["jose", "pedro", "diego"]
# print(piezas_posibles([1,2], personas))


a = [1, 2, 3, 4]
b = [2, 1, 3, 4]

#print(len(set(a) ^ set(b)))
