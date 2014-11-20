import sys
ramos=[]
personas=[]
numeros=[]
siglas=[]
numeros_i=[]
siglas_i=[]
entrada=''

while True:
    entrada=str(sys.stdin.readline())
    entrada=entrada.replace('\n','')
    if entrada=='#':
        break
    persona,numero=entrada.split(',')
    personas.append(persona)
    numeros.append(numero)

entrada2=''
while True:
    entrada2=str(sys.stdin.readline())
    entrada2=entrada2.replace('\n','')
    if entrada2=='#':
        break
    ramo,sigla=entrada2.split(',')
    ramos.append(ramo)
    siglas.append(sigla)
    
entrada3=''
while True:
    entrada3=str(sys.stdin.readline())
    entrada3=entrada3.replace('\n','')
    if entrada3=='':
        break
    numeri,siglai=entrada3.split(',')
    numeros_i.append(numeri)
    siglas_i.append(siglai)
    
i=0
while i<len(siglas_i):
    perso=personas[numeros.index(numeros_i[i])]
    ram=ramos[siglas.index(siglas_i[i])]
    print(perso+','+ram)
    i+=1
