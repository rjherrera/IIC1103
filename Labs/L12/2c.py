a = [['a', 'b', 'c'], ['a', 'c', 'b'], ['c', 'b', 'a'],
     ['b', 'c', 'a'], ['b', 'a', 'c'], ['c', 'a', 'b']]

piezas = [2,1]


def pieza(posibles, piezas):
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






b = pieza(a, piezas)

for i in b:
    print(b)
