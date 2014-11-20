import sys

class Recta():

    def __init__(self, m, n):
        self.pendiente = int(m)
        self.coeficiente = int(n)

    def __str__(self):
        return str(self.pendiente)+'x+'+str(self.coeficiente)

    def paralelos(self, recta, rectas):
        pass

    
a = int(sys.stdin.readline().strip())
rectas = []
i = 0
while i < a:
    b = sys.stdin.readline().strip().split(' ')
    recta = Recta(b[0],b[1])
    rectas.append(recta)
    i += 1

for i in range(len(rectas)):
    string = str(rectas[i])
    stringf = str(rectas[i])
    for j in range(len(rectas)):
        if rectas[i].pendiente == rectas[j].pendiente and i<j:
            stringf += '||'+str(rectas[j])
    if stringf != string:
        print(stringf)
