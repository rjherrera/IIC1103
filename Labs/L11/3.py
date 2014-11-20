import sys


def es_suma(numero, lista):
    if numero == 0:
        return True
    elif numero < 0:
        return False
    for i in lista:
        if es_suma(numero - i, lista):
            return True
    return False


a = sys.stdin.readline().strip().split(',')
b = int(sys.stdin.readline().strip())

for i in range(len(a)):
    a[i] = int(a[i])

print(es_suma(b, a))
