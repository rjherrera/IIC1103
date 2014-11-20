import sys

def anagrama(palabras):
    palabras=palabras.lower()
    palabras=palabras.replace(' ','')
    palabras=palabras.split('-')
    suma1=0
    suma2=0
    suma3=0
    for i in palabras[0]:
        for j in palabras[1]:
            if i==j:
                suma1+=1
        for k in palabras[2]:
            if i==k:
                suma2+=1
    for l in palabras[1]:
        for m in palabras[2]:
            if l==m:
                suma3+=1
    print (suma1,suma2,suma3)
    if suma1==len(palabras[0]) or suma2==len(palabras[0]) or suma3==len(palabras[0]):
        if suma1==suma2:
            return 2
        return 1
    return 0
        
        
    
    
    

plbrs=str(input())
print(anagrama(plbrs))
