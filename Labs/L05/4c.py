def anagr(frase):
    frase = frase.replace(" ", "").lower()
    palabras = frase.split('-')
 
    a=''.join(sorted(palabras[0]))
    b=''.join(sorted(palabras[1]))
    c=''.join(sorted(palabras[2]))
    cant=0
    if palabras[0]==palabras[1]:
        cant+=0
    elif a==b:
        cant+=1
    if palabras[0]==palabras[2]:
        cant+=0
    elif a==c:
        cant+=1
    else:
        cant+=0
    return cant
 
frs=str(input())
print(anagr(frs))
