import sys
a=int(sys.stdin.readline().strip())
b=int(sys.stdin.readline().strip())
c=int(sys.stdin.readline().strip())
if (a<(b+c) and b<(a+c) and c<(b+a))and((a>(abs(b-c)))and(b>(abs(a-c)))and(c>(abs(b-a)))):
    print('True')
else:
    print ('False')
