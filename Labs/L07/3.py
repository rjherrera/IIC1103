import sys
a = sys.stdin.readline()
a = a.replace('\n','')
a = a.split(' ')
a[0], a[1] = int(a[0]), int(a[1])
lista = []
otros = []

i = 0
while i < a[0]:
    b = sys.stdin.readline()
    b = b.replace('\n','')
    b = b.split(' ')
    for j in range(len(b)):
        b[j] = int(b[j])
    lista.append(tuple(b))
    i += 1

i = 0
while i < len(lista):
    if len(lista[i]) - 1 < a[1]:
        otros.append(lista[i])
        lista.remove(lista[i])
        i -= 1
    i += 1

otros.sort()
lista.sort(key=lambda lista: lista[a[1]], reverse=True)

for i in lista:
    a = ''
    for j in i:
        a += str(j) + ' '
    print(a[:-1])

for i in otros:
    a = ''
    for j in i:
        a += str(j) + ' '
    print(a[:-1])
