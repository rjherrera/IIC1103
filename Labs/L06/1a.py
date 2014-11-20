import sys
def lhista():
    lista=[]
    n=""
    while n!="#":
        n=str(sys.stdin.readline())
        n=n.replace("\n","")
        if n=="#":
            break
        q=n.split(",")
        lista.append(q)
    return lista
a=lhista()
b=lhista()
def lizta():
    lista=[]
    n="a"
    while n!="":
        n=str(sys.stdin.readline())
        n=n.replace("\n","")
        if n=="":
            break
        q=n.split(",")
        lista.append(q)
    return lista
c=lizta()
def listta(lhista,lizta,listta):
    for i in listta:
        r=i[0]
        s=i[1]
        for j in lhista:
            if j[1]==r:
                l=j[0]
                break
        for k in lizta:
            if k[1]==s:
                print(l+","+k[0])
                break
listta(a,b,c)

                
                
    
    
    
