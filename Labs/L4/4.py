import sys
def es_primo(x):
    esprimo=True
    n=2
    while esprimo and n<x:
        a=x%n
        if a==0:
            esprimo=False
        n+=1
    if x==1:
        esprimo=False
    return(esprimo)

def digitear(x):
    i=0
    digitos=[]
    while x>0:
        digitos.append(x%10)
        x//=10
        i+=1
    return(digitos)

def factoresp(n):
    i=n-1
    factores=[]
    while i>0:
        if n%i==0 and es_primo(i):
            factores.append(i)
        i-=1
    return(factores)

def digiteartotal(n):
    fact=factoresp(n)
    digfac=[]
    for i in fact:
        digfac.extend(digitear(i))
    return (digfac)

def es_numero_smith(n):
    digitosnumerosumar=digitear(n)
    digitosprimosumar=digiteartotal(n)
    suma=0
    suma1=0
    for i in digitosnumerosumar:
        suma+= i
    for j in digitosprimosumar:
        suma1+= j
    if suma1==suma:
        return True
    else: return False
    
n=int(sys.stdin.readline())
print(es_numero_smith(n))
