import sys
a = sys.stdin.readline()
lista = []
while a != '':
    a = a.replace('\n','')
    a = a.replace(' ', '')
    a = a.split(',')
    lista.append((a[0], int(a[1])))
    lista.sort()
    a = sys.stdin.readline()

for i, j in lista:
    print(i + ',' + str(j))  # espacio?
