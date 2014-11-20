import sys
n1=int(sys.stdin.readline().strip())
n2=int(sys.stdin.readline().strip())
acarreo=0
sobra=0
while n1>=1 or n2>=1:
    a=n1%10
    b=n2%10
    if a+b+sobra>=10:
        acarreo+=1
        sobra=1
    else:
        sobra=0
    n1//=10
    n2//=10
print(acarreo)
