import sys
n=int(sys.stdin.readline())
m=int(sys.stdin.readline())
largo=(len(str(m)))
cont=0
nuevo=0
def separar(x): 
    return list(map(int, str(x)))
lista=separar(m)

while cont<largo:
    h=(m%10)*(n**cont)
    nuevo+=h
    cont+=1
    m//=10
i=1
a=0

while i<largo:
    if lista[i]>(n-1):
        a+=1
    i+=1

if a!=0:
    print('-1')
else:
    print(nuevo)
