import sys
c1 = int(sys.stdin.readline())
c2 = int(sys.stdin.readline())
c3 = int(sys.stdin.readline())
c4 = int(sys.stdin.readline())
c5 = int(sys.stdin.readline())
c6 = int(sys.stdin.readline())
c7 = int(sys.stdin.readline())
c8 = int(sys.stdin.readline())
c9 = int(sys.stdin.readline())
c10 = int(sys.stdin.readline())
precio = int(sys.stdin.readline())
pago = int(sys.stdin.readline())

valor = [20000, 10000, 5000, 2000, 1000, 500, 100, 50, 10, 1]
cantidad = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]
result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
i = 0
a = 0
b=0
c=0
vuelto = pago - precio
devuelto=0
while vuelto > 0 and i<10:
    if ((vuelto) // (valor[i]))>cantidad[i]:
        result[i]=cantidad[i]
    else:
        result[i]=(vuelto) // (valor[i])
    if result[i] != 0:
        vuelto -= (valor[i]) * (result[i])
    i += 1

while c<10:
    dado=result[c]*valor[c]
    devuelto+=dado
    c+=1

if vuelto>devuelto:
    print('-1')
else:
    while b<10:
        if result[b]!=0:
            print(result[b])
            print(valor[b])
        b+=1
