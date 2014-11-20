import sys

def anagpar(palabra1,palabra2):
    s1=0
    j=0
    for i in palabra1:
        j=0
        while j<len(palabra2):
            if palabra2[j]==i:
                s1+=1
                break
            j+=1
    if palabra1!=palabra2 and s1==len(palabra1):
        return True
    return False
        
def anagrama(palabras):
    palabras=palabras.lower()
    palabras=palabras.replace(' ','')
    palabras=palabras.split('-')
    if anagpar(palabras[0],palabras[1]) or anagpar(palabras[0],palabras[2]) or anagpar(palabras[1],palabras[2]):
        if anagpar(palabras[0],palabras[1]) and anagpar(palabras[0],palabras[2]) and anagpar(palabras[1],palabras[2]):
            return 2
        return 1
    return 0

plbrs=str(input())
print(anagrama(plbrs))
