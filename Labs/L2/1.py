import sys
a=int(sys.stdin.readline().strip())
b=int(sys.stdin.readline().strip())
c=int(sys.stdin.readline().strip())
lista = [a, b, c]
lista = list(set(lista))
repe=len(lista)
if repe==1:
    print('3')
elif repe==2:
    print('2')
elif repe==3:
    print('0')
