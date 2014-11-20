import sys
def es_primo(n):
    for i in range(2,n//2):
        d=(n%i!=0)
        if d==False:
            d=0
            return d
    d=1
    return d
def es_numero_smith(n):
    primos=[]
    sumaprimos=0
    for i in range (2,n//2+1):
        m=n
        while es_primo(i)==1 and m%i==0:
            m=m/i
            primos.append(i)
    for i in range (0, len(primos)):
        primostring=str(primos[i])
        for x in primostring:
            sumaprimos+=int(x)
    sumadigitos=0
    n2=str(n)
    for x in n2:
        sumadigitos+=int(x)
    d=(sumaprimos==sumadigitos)
 
    return d
n=int(sys.stdin.readline())
print(es_numero_smith(n))
