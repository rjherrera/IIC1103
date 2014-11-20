import sys


def find_pos(letra, string):
    pos = []
    for i in range(len(string)):
        if string[i] == letra:
            pos.append(i)
    return pos


def suma_valida(string):
    if string.isdigit():
        return True
    for i in find_pos('+', string):
        if suma_valida(string[1:i]) and suma_valida(string[i + 1:-1]):
            return True
    return False

a = sys.stdin.readline().strip()

print(suma_valida(a))
