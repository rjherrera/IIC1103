import sys
def probabilidad(l1, l2, l3, L):
    prob=0
    a=l1
    a_2=l2
    b=l2-l1
    c=l3-l2
    d=l3-l1
    e=100-l2
    f=100-l3
    #caso l1 l2
    if L<a or L<b or L<e:
        prob+=1
    #caso l1 l3   
    if L<a or L<d or L<f:
        prob+=1
    #caso l2 l3
    if L<a_2 or L<c or L<f:
        prob+=1
    prob=prob/3
    return(prob)

x=int(sys.stdin.readline())
y=int(sys.stdin.readline())
z=int(sys.stdin.readline())
w=int(sys.stdin.readline())

print(probabilidad(x,y,z,w))

        
