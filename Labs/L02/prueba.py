import sys
numero=int(sys.stdin.readline().strip())
def separar(x): 
    return list(map(int, str(x)))
digitos=separar(numero)
largo=(len(str(numero)))-1
n=0
verdades=0
while largo>n:
    if digitos[n]==digitos[largo]:
        n=n+1
        largo=largo-1
        verdades=n
    else:
        n=largo
        verdades=0

if verdades==(len(str(numero)))//2:
    print('True')
else:
    print('False')
