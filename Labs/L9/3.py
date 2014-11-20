import sys

class Cliente():

    def __init__(self, usuario, plata):
        self.nombre = usuario
        self.saldo = int(plata)

    def __str__(self):
        return self.nombre+','+str(self.saldo)

    def transaccion(self, destino, plata):
        if self.saldo >= int(plata):
            self.saldo -= int(plata)
            destino.saldo += int(plata)


clientes = []
a = sys.stdin.readline().strip()
while a != 'transacciones':
    a = a.split(',')
    cliente = Cliente(a[0], a[1])
    clientes.append(cliente)
    a = sys.stdin.readline().strip()

b = sys.stdin.readline().strip()
while b != 'balance':
    b = b.split(',')
    for i in clientes:
        if i.nombre == b[0]:
            de = i
        elif i.nombre == b[1]:
            para = i
    de.transaccion(para, b[2])
    b = sys.stdin.readline().strip()
    
for i in clientes:
    print(i)
