import sys

class Recta():

    def __init__(self, m, n):
        self.pendiente = int(m)
        self.coeficiente = int(n)

    def contiene_a(self, punto):
        return punto.y == self.pendiente * punto.x + self.coeficiente


class Punto():

    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

a = sys.stdin.readline().strip().split(' ')
recta = Recta(a[0],a[1])
b = sys.stdin.readline().strip()
while b!='salir':
    b = b.split(' ')
    punto = Punto(b[0],b[1])
    print(recta.contiene_a(punto))
    b = sys.stdin.readline().strip()

print('bye')
