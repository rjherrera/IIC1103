import sys

class Poker():

    def __init__(self, mano):
        for i in range(len(mano)):
            if mano[i][:-1]=='Jack' or mano[i][:-1]=='J':
                mano[i]='11'+mano[i][len(mano[i])-1]
            elif mano[i][:-1]=='Queen' or mano[i][:-1]=='Q':
                mano[i]='12'+mano[i][len(mano[i])-1]
            elif mano[i][:-1]=='King' or mano[i][:-1]=='K':
                mano[i]='13'+mano[i][len(mano[i])-1]
            elif mano[i][:-1]=='A':
                mano[i]='14'+mano[i][len(mano[i])-1]
        self.c1, self.c2, self.c3 = mano[0], mano[1], mano[2]
        self.c4, self.c5 = mano[3], mano[4]
        self.mano1 = [int(mano[0][:-1]),int(mano[1][:-1]),int(mano[2][:-1]),int(mano[3][:-1]),int(mano[4][:-1])]

    def __rshift__(self, otra):
        self.mano1.sort()
        otra.mano1.sort()
        return self.mano1[len(self.mano1)-1] > otra.mano1[len(self.mano1)-1]

    def __gt__(self, otra):
        sm, so = 0, 0
        for i in range(len(self.mano1)):
            sm += self.mano1[i]
            so += otra.mano1[i]
        return sm > so

    def iguales(self):
        ig = 0
        for i in range(len(self.mano1)):
            for j in range(len(self.mano1)):
                if self.mano1[i]==self.mano1[j] and i<j:
                    ig += 1
        return ig
                

    def ranking(self, jug2):
        if self>>jug2:
            return 'Gana Jugador 1'
        elif jug2>>self:
            return 'Gana Jugador 2'
        elif self.iguales() == 1 and jug2.iguales() != 1:
            return 'Gana Jugador 1'
        elif self.iguales() == 2 and (jug2.iguales() > 2 or jug2.iguales() == 0):
            return 'Gana Jugador 1'
        elif jug2.iguales() == 1 and self.iguales() != 1:
            return 'Gana Jugador 2'
        elif jug2.iguales() == 2 and (self.iguales() > 2 or self.iguales() == 0):
            return 'Gana Jugador 2'
        else:
            if self>jug2:
                return 'Gana Jugador 1'
            else:
                return 'Gana Jugador 2'




a = sys.stdin.readline().strip().split(' ')
b = sys.stdin.readline().strip().split(' ')

j1 = Poker(a)
j2 = Poker(b)


print('Gana Jugador 2')
