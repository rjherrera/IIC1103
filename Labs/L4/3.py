import sys
def es_perfecto(n):
    sumadivs=0
    div=1
    while div<n:
        if n%div==0:
            sumadivs+=div
        div+=1
    if sumadivs==n:
       return True
    else:
        return False
 
def es_par(n):
    if n%2==0:
       return True
    else:
       return False
 
def es_cuadrado_perfecto(n):
   if (n**(1/2))%1==0:
     return True
   else:
     return False 
 
def mcd(a,b):
    maximo=0
    i=1
    while i<=a and i<=b:
        if a%i==0 and b%i==0:
            maximo=i
        i=i+1
    return maximo
        
def salir():
    print('bye!')
 
primero=0
while primero!='salir':
    primero=sys.stdin.readline().strip()
    if primero=='es_perfecto':
        b=int(sys.stdin.readline())
        print(es_perfecto(b))
    elif primero=='es_par':
        b=int(sys.stdin.readline())
        print(es_par(b))
    elif primero=='es_cuadrado_perfecto':
        b=int(sys.stdin.readline())
        print(es_cuadrado_perfecto(b))
    elif primero=='mcd':
        b=int(sys.stdin.readline())
        c=int(sys.stdin.readline())
        print(mcd(b,c))
salir()
