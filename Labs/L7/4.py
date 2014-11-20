import sys
a = sys.stdin.readline()
a = a.replace('\n','')
a = a.split(' ')
a[0], a[1] = int(a[0]), int(a[1])
lista = []


def factores(n):
    lista = []
    i = 2
    while n > 1:
        while n % i == 0:
            lista.append(i)
            n //= i
        i += 1
    return list(set(lista))  # return lista

i = 0
while i < a[1]:
    b = sys.stdin.readline()
    lista.append((int(b), factores(int(b))))
    i += 1

num = a[0], list(set(factores(a[0])))
l = 0
comunes = []
for i, j in lista:
    coinc = [x for x in j if x in num[1]]
    comunes.append((len(coinc), i))
    comunes.sort(reverse=True)

for i, j in comunes:
    print(j)
