import sys

def decodificar(encriptado):
    decof=''
    if '\n' in encriptado:
        encriptado=encriptado[:len(encriptado)-1]
    largo=len(encriptado)/8
    i=0
    while i<largo:
        decof+=chr(int(encriptado[:8],2))
        encriptado=encriptado[8:]
        i+=1
    return decof[::-1]

encr=str(input())
print(decodificar(encr))
