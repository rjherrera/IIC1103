c1 = 2
c2 = 3
c3 = 8
c4 = 1
c5 = 11
c6 = 15
c7 = 25
c8 = 30
c9 = 50
c10 = 70
precio = int(input('monto a precio'))
pago = int(input('cantidad pagada'))


valor = [20000, 10000, 5000, 2000, 1000, 500, 100, 50, 10, 1]
cantidad = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]
result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
i = 0
a = 0
b = 0
vuelto = pago - precio

def caja():
    global valor, cantidad, result, i, a, b, vuelto
    while vuelto > 0:
        result[i]=(vuelto) // (valor[i])
        if (vuelto // valor[i]) != 0:
            vuelto -= (valor[i]) * (vuelto // valor[i])
        i += 1
    while vuelto == 0:
        if result[a] > cantidad[a]:
            nuevo = (result[a] - cantidad[a]) * valor[a]
            vuelto += nuevo
        elif result[a] <= cantidad[a]:
            b += 1
        a += 1
        i = a
    
print (a,vuelto)
print(result)
