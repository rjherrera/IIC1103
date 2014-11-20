polinomio=input()
#numero=input()
pol=[]
polin=''
for i in polinomio:
    if i=='-':
        pol.append('+')
    else:
        pol.append(i)
for i in pol:
    polin+=str(i)
print(polin)
        
        
    
        
print(polin.split('+'))

    
