import sys
 
def probabilidad(l1, l2, l3, L):
    a=l1
    b=l2-l1
    c=l3-l2
    prob=float(0)
    if L<c:
        prob+=1/3
    if L<b:
        prob+=1/3
    if L<a:
        prob+=1/3
    return(prob)
 
x=int(sys.stdin.readline())
y=int(sys.stdin.readline())
z=int(sys.stdin.readline())
w=int(sys.stdin.readline())
 
print(probabilidad(x,y,z,w))