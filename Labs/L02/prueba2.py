import sys
lista = [int(sys.stdin.readline().strip()), int(sys.stdin.readline().strip()), int(sys.stdin.readline().strip())]
lista = list(set(lista))
repe=len(lista)
if repe==1:
    print('3')
elif repe==2:
    print('2')
elif repe==3:
    print('0')
