import sys

a=sys.stdin.readline()
largo,pedidos=a.split(' ')
pedidos=pedidos.replace('\n','')
frases=[]
lista=[]

i=0
while i<int(largo):
    a=sys.stdin.readline()
    a=a.replace('\n','')
    frases.append(a)
    i+=1

j=0
while j<int(pedidos):
    cantidad=0
    b=sys.stdin.readline()
    b=b.replace('\n','')
    x=b.split('-')
    for i in frases:
        if i.count(x[1])>=int(x[0]):
            cantidad+=1
    lista.append(cantidad/len(frases))
    j+=1

for i in lista:
    j=str(i)
    while len(j)<4:
        j+='0'
    print(j[:4])
