import sys
a = sys.stdin.readline().strip().split(' ')

i=0
matriz = []

while i < int(a[0]):
    b = sys.stdin.readline().strip().split(' ')
    matriz.append(b)
    i+=1
i=0
j=0
suma = int(matriz[0][0])
while i<len(matriz):
    if i+1 > len(matriz)-1 and j+1 > len(matriz[0])-1:
        break
    elif i+1 > len(matriz)-1:
        suma += int(matriz[i][j+1])
        j+=1
    elif j+1 > len(matriz[0])-1:
        suma += int(matriz[i+1][j])
        i+=1
    elif int(matriz[i][j+1]) > int(matriz[i+1][j]):
        suma += int(matriz[i+1][j])
        i+=1
    elif int(matriz[i][j+1]) < int(matriz[i+1][j]):
        suma += int(matriz[i][j+1])
        j+=1

print(suma)
