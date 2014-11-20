import sys
a = sys.stdin.readline().strip().split(' ')

i=0
matriz = []

while i < int(a[0]):
    b = sys.stdin.readline().strip().split(' ')
    matriz.append(b)
    i+=1

escalar = sys.stdin.readline().strip()

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        matriz[i][j] = float(matriz[i][j])*float(escalar)

for i in matriz:
    x = ''
    for j in i:
        x += str(j) + ' '
    print(x[:-1])
