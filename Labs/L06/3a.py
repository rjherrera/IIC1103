import sys
 
NH = sys.stdin.readline()
nh = NH.split()
N=int(nh[0])
H=int(nh[1])
x= sys.stdin.readline()
x1 = x.split()
X=[]
for n in x1:
    X.append(int(n)) # lista con todos los x (x,...)
XY=[]   
for i in range(0,N-1):
    xy=[]
    entra = sys.stdin.readline().strip()
    ent = entra.split()
    entrada=[]
    for n in ent:
        entrada.append(int(n))
    for w in range(0,len(entrada)):
        xy.append((X[w],entrada[w]))
    XY.append(xy)
 
def pendiente(p1,p2):
    return((p2[1]-p1[1])/(p2[0]-p1[0]))
 
for puntos in XY:
    for lugar in range(0,len(puntos)-1):
        print(str(pendiente(puntos[lugar],puntos[lugar+1])),end=' ')
    print('')
