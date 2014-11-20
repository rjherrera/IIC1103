import tableroGUI
import random
tablero = None 
a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p = (0,)*16
puntaje = 0
def inicia_juego():
    global a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p
    a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p = tablero.inicia_juego()

def actualizar_tablero():
    global a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p
    tablero.update(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p, puntaje)

def esperar_presionar_tecla():
    return tablero.esperarPresionarTecla()  
    
def aleatorio():
    return tablero.aleatorio()

def tarea(tablero):
    global puntaje,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p
    #Aqui empieza tu tarea
    
    inicia_juego()
    puntaje = pt(a) + pt(b) + pt(c) + pt(d) + pt(e) + pt(f) + pt(g) + pt(h) + pt(i) + pt(j) + pt(k) + pt(l) + pt(m) + pt(n) + pt(o) + pt(p)
    actualizar_tablero()
    while True:
        pa, pb, pc, pd, pe, pf, pg, ph, pi, pj, pk, pl, pm, pn, po, pp = a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p
        tecla = esperar_presionar_tecla()
        if tecla == 'arriba':
            a, b, c, d, e, f, g, h = movimiento(a, b, c, d, e, f, g, h)
            e, f, g, h, i, j, k, l = movimiento(e, f, g, h, i, j, k, l)
            i, j, k, l, m, n, o, p = movimiento(i, j, k, l, m, n, o, p)
            if not (pa == a and pb == b and pc == c and pd == d and pe == e and pf == f and pg == g and ph == h and pi == i and pj == j and pk == k and pl == l and pm == m and pn == n and po == o and pp == p):
                (m, n, o, p) = agregar(m, n, o, p)
        elif tecla == 'abajo':
            m, n, o, p, i, j, k, l = movimiento(m, n, o, p, i, j, k, l)
            i, j, k, l, e, f, g, h = movimiento(i, j, k, l, e, f, g, h)
            e, f, g, h, a, b, c, d = movimiento(e, f, g, h, a, b, c, d)
            if not (pa == a and pb == b and pc == c and pd == d and pe == e and pf == f and pg == g and ph == h and pi == i and pj == j and pk == k and pl == l and pm == m and pn == n and po == o and pp == p):
                (a, b, c, d) = agregar(a, b, c, d)
        elif tecla == 'derecha':
            d, h, l, p, c, g, k, o = movimiento(d, h, l, p, c, g, k, o)
            c, g, k, o, b, f, j, n = movimiento(c, g, k, o, b, f, j, n)
            b, f, j, n, a, e, i, m = movimiento(b, f, j, n, a, e, i, m)
            if not (pa == a and pb == b and pc == c and pd == d and pe == e and pf == f and pg == g and ph == h and pi == i and pj == j and pk == k and pl == l and pm == m and pn == n and po == o and pp == p):
                (a, e, i, m) = agregar(a, e, i, m)
        elif tecla == 'izquierda':
            a, e, i, m, b, f, j, n = movimiento(a, e, i, m, b, f, j, n)
            b, f, j, n, c, g, k, o = movimiento(b, f, j, n, c, g, k, o)
            c, g, k, o, d, h, l, p = movimiento(c, g, k, o, d, h, l, p)
            if not (pa == a and pb == b and pc == c and pd == d and pe == e and pf == f and pg == g and ph == h and pi == i and pj == j and pk == k and pl == l and pm == m and pn == n and po == o and pp == p):
                (d, h, l, p) = agregar(d, h, l, p)
        puntaje = pt(a) + pt(b) + pt(c) + pt(d) + pt(e) + pt(f) + pt(g) + pt(h) + pt(i) + pt(j) + pt(k) + pt(l) + pt(m) + pt(n) + pt(o) + pt(p)
        actualizar_tablero()
        
def pt(x):
    i = 0
    puntos = 0
    if x > 2:
        n = x / 3
        while n != 1:
            n = n / 2
            i = i + 1
        puntos = 3 ** (i + 1)
    return int(puntos)

def mov(x, y):
    if ((x == y and x >= 3) or (x == 2 and y == 1) or (x == 1 and y == 2) or x == 0 or y == 0):
        x = x + y
        y = 0
    return (x, y)

def movimiento(a1, b1, c1, d1, e1, f1, g1, h1):
    xa, xe = mov(a1, e1)
    xb, xf = mov(b1, f1)
    xc, xg = mov(c1, g1)
    xd, xh = mov(d1, h1)
    return(xa, xb, xc, xd, xe, xf, xg, xh)

def agregar(x, y, z, w):
    px, py, pz, pw = x, y, z, w
    while (px == x and py == y and pz == z and pw == w):
        randomio = random.randint(1, 4)
        if x == 0 and randomio == 1:
            x = aleatorio()
        elif y == 0 and randomio == 2:
            y = aleatorio()
        elif z == 0 and randomio == 3:
            z = aleatorio()
        elif w == 0 and randomio == 4:
            w = aleatorio()
    return (x, y, z, w)
    #Aqui termina tu tarea

tablero = tableroGUI.Application("tarea")
tablero.title('DCC - Threes')
tablero.loadProgram(tarea)
tablero.start()
