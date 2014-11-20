import sys

def parentesis(frase):
    if frase.count('(')==frase.count(')') and frase.index('(')<frase.index(')'):
        i=0
        while i<len(frase)-1:
            if frase[i]=='(' and frase[i+1]==')':
                return False
            i+=1
        return True
    return False

texto=str(input())
print(parentesis(texto))
