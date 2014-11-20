import sys
total = 0
plata = 0
while True:
    d = sys.stdin.readline().strip()
    if d == 'donar':
        plata = int(sys.stdin.readline().strip())
        if plata>=100 and plata<=(10**5):
            total += plata
        else:
            total=total
    elif d == 'reportar':
        print(total)
    elif d=='0':
        break
