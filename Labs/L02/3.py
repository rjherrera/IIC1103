import sys
a=float(sys.stdin.readline().strip())
b=float(sys.stdin.readline().strip())
c=float(sys.stdin.readline().strip())
disc=(b**2)-(4*a*c)
if a==0:
    print('no es ecuacion cuadratica')
elif disc>0:
    print('ecuacion cuadratica con raices reales distintas')
elif disc==0:
    print('ecuacion cuadratica con raices reales iguales')
elif disc<0:
    print('ecuacion cuadratica con raices complejas')
