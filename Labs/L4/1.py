import sys
def es_primo(x):
    esprimo=True
    n=2
    while esprimo and n<x:
        a=x%n
        if a==0:
            esprimo=False
        n+=1
    return(esprimo)
    
def es_mala_onda(x):
    while x>=5 and x%5==0:
        x=x/5
    while x>=3 and x%3==0:
        x=x/3
    while x>=2 and x%2==0:
        x=x/2
    if x==1:
        return True
    elif x!=1:
        return False


n=int(sys.stdin.readline())
x=1
i=1
while i<=n:
    if es_mala_onda(x):
        enesimo=x
        x+=1
        i+=1
    if not es_mala_onda(x):
        x+=1
print(enesimo)
