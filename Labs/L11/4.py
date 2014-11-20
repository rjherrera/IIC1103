import sys


def camion(precio, volumen, cosas):
    suma_precio = 0
    suma_volumen = 0
    for i, j in cosas:
        suma_volumen += i
        suma_precio += j
    if suma_precio > precio and suma_volumen < volumen:
        return True
    for i in range(len(cosas)):
        if camion(precio, volumen, cosas[:i] + cosas[i + 1:]):
            return True
    return False


a = int(sys.stdin.readline().strip())
b = int(sys.stdin.readline().strip())
c = []

entrada = sys.stdin.readline().strip()

while entrada != '':
    entrada = entrada.split(',')
    entrada = [int(entrada[i]) for i in range(len(entrada))]
    c.append(tuple(entrada))
    entrada = sys.stdin.readline().strip()

print(camion(a, b, c))
