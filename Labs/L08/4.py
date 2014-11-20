import sys

a = sys.stdin.readline().strip()

i=0
matriz = []

while i < int(a):
    b = list(sys.stdin.readline().strip())
    matriz.append(b)
    i+=1

joya = 0
for i in matriz[0]:
    suma = 1
    for j in range(1,len(matriz)):
        if matriz[j].count(i)>0:
            suma+=1
    if suma>=len(matriz):
        joya+=1
            
print(joya)
