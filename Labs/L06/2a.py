polin=input()
n=input()
lista=[]
for i in polin:
    lista.append(i)

for i in lista:
    if i=='^' or i=='*':
        lista.remove(i)
        
for i in range(len(lista)):
    if lista[i]=='x':
        lista[i]=n

string=''
for i in lista:
    string+=i
suma=[]
resta=[]

for i in range(len(string)-1):
    if string[i]=='+':
        suma.append(string[i+1])
        suma.append(string[i+2])
        suma.append(string[i+3])

for i in range(len(string)-1):
    if string[i]=='-':
        resta.append(string[i+1])
        resta.append(string[i+2])
        resta.append(string[i+3])

if string[0]!='-':
    suma.append(string[0])
    suma.append(string[1])
    suma.append(string[2])

def calculo(lista):
    suma=0
    for i in range(len(lista)):
        lista[i]=int(lista[i])
    i=1
    while i<len(lista):
        suma+=(lista[i]**lista[i+1])*lista[i-1]
        i+=3
    return suma

print(calculo(suma)-calculo(resta))  
    
