import sys

def palindromo(texto):
    texto=texto.replace(' ','')
    texto=texto.replace('\n','')
    texto=texto.replace('á','a')
    texto=texto.replace('é','e')
    texto=texto.replace('í','i')
    texto=texto.replace('ó','o')
    texto=texto.replace('ú','u')
    texto=texto.lower()
    for i in texto:
        if not 97<=ord(i)<=122:
            texto=texto.replace(i,'')
    if texto[::-1]==texto:
        return True
    return False

txt=str(input())
print(palindromo(txt))
