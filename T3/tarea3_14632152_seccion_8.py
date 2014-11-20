import instaintro_gui


def tarea():
    # Aqui empieza tu tarea
    c = [[1, 2, 1],[0, 0, 0],[-1, -2, -1]]
    while True:
        click = instaintro_gui.esperar_click()
        imagen = instaintro_gui.obtener_pixeles()
        if click == 'salir':
            instaintro_gui.salir()
        elif imagen != None and click != -1:
            if click == 'girar':
                imagen = girar(imagen)
            elif click == 'gris':
                grises(imagen)
            elif click == 'bordes':
                imagen = bordes(imagen, c)
            elif click == 'mosaico':
                gifs = instaintro_gui.obtener_imagenes_mosaico()
                mosaico(gifs, imagen)
            instaintro_gui.actualizar_imagen(imagen)


def grises(matriz):
    for i in matriz:
        for j in range(len(i)):
            pr = (i[j][0] + i[j][1] + i[j][2]) // 3
            i[j] = (pr, pr, pr)


def girar(matriz):
    girado = []
    for i in range(len(matriz[0])):
        fila = []
        for j in matriz:
            fila.insert(0, j[i])
        girado.append(fila)
    return girado


def convolucion(matriz, operador):
    g = [[(0, 0, 0)] * len(matriz[0]) for i in range(len(matriz))]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            for k in range(3):
                for l in range(3):
                    m, n = i + k - 1, j + l - 1
                    if -1 < m < len(matriz) and -1 < n < len(matriz[0]):
                        pixel = matriz[m][n]
                    else:
                        pixel = (0, 0, 0)
                    g[i][j] = tuple(m + n for m, n in zip(
                        g[i][j], tuple(o * operador[k][l] for o in pixel)))
    return g
    

def bordes(matriz, operador):
    grises(matriz)
    g = [[(0, 0, 0)] * len(matriz[0]) for i in range(len(matriz))]
    gy = convolucion(matriz, operador)
    gx = convolucion(matriz, girar(operador))
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            px = tuple(int((k ** 2 + l ** 2) ** (1 / 2))
                       for k, l in zip(gx[i][j], gy[i][j]))
            nt = max(px[0], px[1], px[2], 255) / 255
            g[i][j] = (int(px[0] / nt), int(px[1] / nt), int(px[2] / nt))
    return g


def subimagenes(lista):
    subs = []
    i = 5
    while i <= len(lista):
        j = 5
        while j <= len(lista[0]):
            sub = []
            for k in range(i - 5, i):
                sub.append(lista[k][j - 5:j])
            subs.append(sub)
            j += 5
        i += 5
    return subs


def diferencia(lista1, lista2):
    dif = 0
    for i, j in zip(lista1, lista2):
        for k, l in zip(i, j):
            for m, n in zip(k, l):
                dif += (m - n) ** 2
    return dif


def igualdad(lista1, lista2):
    dif = float('infinity')
    for i in lista2:
        d = diferencia(lista1, i)
        if d < dif:
            dif = d
            pos = lista2.index(i)
    return pos


def mosaico(imagenes, matriz):
    porciones = subimagenes(matriz)
    iguales = []
    for i in range(len(porciones)):
        pos = igualdad(porciones[i], imagenes)
        iguales.append(imagenes[pos])
    cols = len(matriz[0])
    u = 0
    for i in range(0, len(matriz) - 5, 5):
        rango = range(u, u + cols // 5)
        for k in range(5):
            matriz[k + i] = []
            for j in rango:
                matriz[k + i].extend(iguales[j][k])
        u += cols // 5


app = instaintro_gui.Application("tarea")
app.title('InstaIntro')
app.loadProgram(tarea)
app.start()
