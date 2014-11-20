import sys


def permutar(string):
    if string == '':
        return ['']
    lista = []
    for i in range(len(string)):
        for j in permutar(string[:i] + string[i + 1:]):
            lista.append(string[i] + j)
    return lista

entrada = sys.stdin.readline().strip()
resultado = permutar(entrada)
for i in resultado:
    print(i)
