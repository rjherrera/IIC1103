import sys

def menor(matriz, i, j, suma):
    if i>0 and j>0 and j<len(matriz[0])-1 and i < len(matriz)-1:
        x = min(matriz[i+1][j],matriz[i][j+1],matriz[i-1][j],matriz[i][j-1])
        if x == matriz[i+1][j]:
            matriz[i+1][j]=10**10
            i+=1
        elif x == matriz[i][j+1]:
            matriz[i][j+1]=10**10
            j+=1
        elif x == matriz[i-1][j]:
            matriz[i-1][j]=10**10
            i-=1
        elif x == matriz[i][j-1]:
            matriz[i][j-1]=10**10
            j-=1
    elif i>0 and j>0 and j<len(matriz[0])-1:
        x = min(matriz[i][j+1],matriz[i-1][j],matriz[i][j-1])
        if x == matriz[i][j+1]:
            matriz[i][j+1]=10**10
            j+=1
        elif x == matriz[i-1][j]:
            matriz[i-1][j]=10**10
            i-=1
        elif x == matriz[i][j-1]:
            matriz[i][j-1]=10**10
            j-=1
    elif i>0 and j>0 and i<len(matriz)-1:
        x = min(matriz[i+1][j],matriz[i-1][j],matriz[i][j-1])
        if x == matriz[i+1][j]:
            matriz[i+1][j]=10**10
            i+=1
        elif x == matriz[i-1][j]:
            matriz[i-1][j]=10**10
            i-=1
        elif x == matriz[i][j-1]:
            matriz[i][j-1]=10**10
            j-=1
    elif i>0 and j>0:
        x = min(matriz[i-1][j],matriz[i][j-1])
        if x == matriz[i-1][j]:
            matriz[i-1][j]=10**10
            i-=1
        elif x == matriz[i][j-1]:
            matriz[i][j-1]=10**10
            j-=1
    elif i>0 and j>0 and i>=len(matriz)-1 and j>=len(matriz[0])-1:
        x = 0
        matriz[len(matriz)][len(matriz)-1]=10**10
        j+=1
        i+=1
    elif i==0 and j==0:
        x = min(matriz[i+1][j],matriz[i][j+1])
        if x == matriz[i+1][j]:
            matriz[i+1][j]=10**10
            i+=1
        elif x == matriz[i][j+1]:
            matriz[i][j+1]=10**10
            j+=1
    elif i==0 and j<len(matriz[0])-1:
        x = min(matriz[i+1][j],matriz[i][j+1],matriz[i][j-1])
        if x == matriz[i+1][j]:
            matriz[i+1][j]=10**10
            i+=1
        elif x == matriz[i][j+1]:
            matriz[i][j+1]=10**10
            j+=1
        elif x == matriz[i][j-1]:
            matriz[i][j-1]=10**10
            j-=1
    elif j==0 and i<len(matriz[0])-1:
        x = min(matriz[i+1][j],matriz[i][j+1],matriz[i-1][j])
        if x == matriz[i+1][j]:
            matriz[i+1][j]=10**10
            i+=1
        elif x == matriz[i][j+1]:
            matriz[i][j+1]=10**10
            j+=1
        elif x == matriz[i-1][j]:
            matriz[i-1][j]=10**10
            i-=1
    elif i==0:
        x = min(matriz[i+1][j],matriz[i][j-1])
        if x == matriz[i+1][j]:
            matriz[i+1][j]=10**10
            i+=1
        elif x == matriz[i][j-1]:
            matriz[i][j-1]=10**10
            j-=1
    elif j==0:
        x = min(matriz[i][j+1],matriz[i-1][j])
        if x == matriz[i][j+1]:
            matriz[i][j+1]=10**10
            j+=1
        elif x == matriz[i-1][j]:
            matriz[i-1][j]=10**10
            i-=1
    else:
        j+=1
        i+=1

    suma += x
    return suma, i, j

a = sys.stdin.readline().strip().split(' ')

i=0
matriz = []

while i < int(a[0]):
    b = sys.stdin.readline().strip().split(' ')
    matriz.append(b)
    i+=1

for i in matriz:
    for j in range(len(i)):
        i[j]=int(i[j])

i = 0
j = 0
suma = matriz[0][0]
matriz[0][0] = 10**8
while not(i == len(matriz)-1 and j == len(matriz[0])-1):
    suma,i,j=menor(matriz,i,j,suma)

print(suma)
    
