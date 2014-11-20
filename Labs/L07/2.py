import sys
a = sys.stdin.readline()
a = a.replace('\n','')
etapas = []
desc = []


def suma(lista, s=0):
    if len(lista) > 2:
        s += int(lista[0]) * 3600 + int(lista[1]) * 60 + int(lista[2])
    return s


def formatear(n):
    h, n = str(n // 3600), n % 3600
    m, n = str(n // 60), n % 60
    s = str(n)
    if len(h) < 2:
        h = '0' + h
    if len(m) < 2:
        m = '0' + m
    if len(s) < 2:
        s = '0' + s
    time = h + ':' + m + ':' + s
    return time


while a != '':
    a = sys.stdin.readline()
    a = a.replace('\n','')
    while a != '':
        a = a.replace('\n','')
        if ',' in a:
            a = a.split(',')
            if not('DES' in a[1]):
                b = a[1].split(':')
                etapas.append([a[0], suma(b)])
            else:
                b = a[1]
                desc.append(a[0])
        a = sys.stdin.readline()
        a = a.replace('\n','')

etapas = [x for x in etapas if x[0] not in desc]
i = 0
while i < len(etapas):
    j = i + 1
    while j < len(etapas):
        if etapas[i][0] == etapas[j][0]:
            etapas[i][1] += etapas[j][1]
            etapas.remove(etapas[j])
            j -= 1
        j += 1
    i += 1

resultados = []
for i, j in etapas:
    resultados.append((i, formatear(j)))

resultados.sort(key=lambda resultados: (resultados[1],resultados[0]))
desc = list(set(desc))
desc.sort()

for i, j in resultados:
    print(i + ',' + j)

for i in desc:
    print(i + ',DES')
