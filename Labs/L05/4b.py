a=0
b = input('')
f=b.replace(" ", "").lower()
c = f.split('-')
 
p=c[0]
t=c[1]
s=c[2]
 
pp=''.join(sorted(p))
tt=''.join(sorted(t))
ss=''.join(sorted(s))
 
if p==t:
    a+=0
elif pp==tt:
    a+=1
 
if p==s:
    a+=0
elif pp==ss:
    a+=1
     
else:
    a+=0
 
print(a)
