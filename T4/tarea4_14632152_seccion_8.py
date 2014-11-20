class Tablero():

    def __init__(self, archivo):
        self.nombre = archivo
        self.fichas = []
        self.arch = open(archivo)
        self.dimensiones = tuple(
            int(i) for i in self.arch.readline().strip().split(','))
        lineas = self.arch.readlines()
        self.prohibidas = [(int(i), int(j)) for i, j in (
            tuple(k.split(',') for k in (l.strip() for l in lineas))) if
            i.isdigit() and -1 < int(i) < self.dimensiones[0] and
            j.isdigit() and -1 < int(j) < self.dimensiones[1]]
        self.arch.close()
        self.rep_matricial = [['0'] * self.dimensiones[1]
                              for i in range(self.dimensiones[0])]
        for i, j in self.prohibidas:
            self.rep_matricial[i][j] = 'X'
        self.outp = []

    def agregar_ficha(self, ficha, posicion):
        ficha.primera_pos = posicion
        ficha.posicion = posicion
        self.fichas.append(ficha)
        for i in self.fichas:
            self.rep_matricial[i.posicion[0]][
                i.posicion[1]] = str(self.fichas.index(i) + 1)
        self.outp.append(str(posicion))

    def mov_pos(self, index_ficha):
        ficha = self.fichas[index_ficha]
        pos_inicial = ficha.posicion
        movs_relativos = ficha.movimientos
        largo = self.dimensiones[0]
        ancho = self.dimensiones[1]
        pos_posibles = []
        for i, j in movs_relativos:
            k = i + pos_inicial[0]
            l = j + pos_inicial[1]
            if -1 < k < largo and -1 < l < ancho and \
                    (i, j) not in self.prohibidas and \
                    self.rep_matricial[k][l] == '0':
                pos_posibles.append((k, l))
        return pos_posibles

    def movimientos_posibles(self, numero_ficha):
        self.reload_rep_matricial()
        ficha = self.fichas[numero_ficha - 1]
        movs = self.mov_pos(numero_ficha - 1)
        string = '\n' + ficha.nombre + ' no se puede mover'
        if len(movs) > 0:
            string = '\n' + ficha.nombre + ' se puede mover a las posiciones '
        for i in range(len(movs)):
            if i == len(movs) - 1 and len(movs) > 1:
                string += ' y ' + str(movs[i])
            elif i > 0:
                string += ', ' + str(movs[i])
            else:
                string += str(movs[i])
        return string

    def avanzar(self, ficha, pos_nueva):
        self.rep_matricial[pos_nueva[0]][
            pos_nueva[1]] = str(self.fichas.index(ficha) + 1)
        ficha.posicion = pos_nueva

    def retroceder(self, ficha, pos_antigua, pos_nueva):
        self.rep_matricial[pos_nueva[0]][pos_nueva[1]] = '0'
        ficha.posicion = pos_antigua

    def se_puede_recorrer(self, archivo_salida):
        tabl = []
        for i in self.rep_matricial:
            for j in i:
                tabl.append(j)
        if '0' not in tabl:
            output = open(archivo_salida, 'x')
            output.write('Recorriendo ' + self.nombre + ' con ')
            for i in range(len(self.outp)):
                if i == len(self.outp) - 1 and len(self.outp) > 1:
                    output.write(' y ' + self.fichas[i].nombre)
                elif i > 0:
                    output.write(', ' + self.fichas[i].nombre)
                else:
                    output.write(self.fichas[i].nombre)
            for i in range(len(self.outp)):
                output.write(
                    '\n' + self.fichas[i].nombre + ': ' + self.outp[i])
            output.close()
            return True
        for i in self.fichas:
            for j in self.mov_pos(self.fichas.index(i)):
                self.outp[self.fichas.index(i)] += '-->' + str(j)  # output
                pos_antigua = i.posicion
                self.avanzar(i, j)
                if self.se_puede_recorrer(archivo_salida):
                    return True
                else:
                    self.retroceder(i, pos_antigua, j)
                    self.outp[self.fichas.index(i)] = self.outp[
                        self.fichas.index(i)][:self.outp[
                            self.fichas.index(i)].rfind('-') - 1]
        return False

    def reload_rep_matricial(self):
        self.rep_matricial = [['0'] * self.dimensiones[1]
                              for i in range(self.dimensiones[0])]
        for i, j in self.prohibidas:
            self.rep_matricial[i][j] = 'X'
        for i in self.fichas:
            self.rep_matricial[i.primera_pos[0]][
                i.primera_pos[1]] = str(self.fichas.index(i) + 1)
            i.posicion = i.primera_pos
        for i in range(len(self.outp)):
            self.outp[i] = self.outp[i][:self.outp[i].find(')') + 1]

    def __str__(self):
        self.reload_rep_matricial()
        tab = self.rep_matricial
        string = '\n'
        for i in range(len(tab)):
            for j in range(len(tab[0])):
                string += tab[i][j] + ' '
            string += '\n'
        string += '\n0: Posición libre | X: Posición prohibida'
        for i in self.fichas:
            string += ' | ' + str(self.fichas.index(i) + 1) + ': ' + i.nombre
        return string


class Ficha():

    def __init__(self, archivo):
        self.nombre = archivo
        self.posicion = None
        self.arch = open(archivo)
        self.movimientos = [(int(i), int(j)) for i, j in (
            tuple(k.split(',') for k in (l.strip() for l in self.arch))) if
            i.replace('-', '').isdigit() and j.replace('-', '').isdigit()]
        self.arch.close()
        self.primera_pos = None


def opciones_inicio():
    print('\n(1) Crear una nueva ficha')
    print('(2) Crear un nuevo tablero')
    print('(3) Cargar un tablero con fichas')
    print('(0) Salir')
    return input('Seleccione una opción: ')


def crear_ficha():
    nombre = input('\nIngrese el nombre del archivo de la nueva ficha: ')
    mov = input('Ingrese un movimiento de la ficha o un 0 para terminar: ')
    movimientos = []
    while mov != '0':
        if mov.replace('-', '', 2).replace(',', '', 1).isdigit() \
                and mov.count(',') == 1 and mov[:mov.find(',')].count('-') < 2\
                and mov.index(',') != 0 and mov.index(',') != len(mov) - 1:
            movimientos.append(mov + '\n')
        else:
            print('Debe ingresar un movimiento válido de la forma "x,y"')
        mov = input('Ingrese un movimiento de la ficha o un 0 para terminar: ')
    if movimientos != []:
        ficha = open(nombre, 'x')
        ficha.writelines(movimientos)
        ficha.close()
        print('-------- ficha', nombre, 'creada correctamente --------')
    else:
        print('No ha ingresado movimientos,', nombre, 'no se ha creado')


def crear_tablero():
    nombre = input('\nIngrese el nombre del archivo del nuevo tablero: ')
    dimensiones = input('Ingrese las dimensiones del tablero: ')
    while not dimensiones.replace(',', '').isdigit() \
            or dimensiones.count(',') != 1 or dimensiones.index(',') == 0 \
            or dimensiones.index(',') == len(dimensiones) - 1:
        print('Debe ingresar dimensiones positivas de la forma "x,y"')
        dimensiones = input('Ingrese las dimensiones del tablero: ')
    pos = input('Ingrese una posición prohibida o un 0 para terminar: ')
    posiciones = []
    while pos != '0':
        if pos.replace(',', '', 1).isdigit() and pos.count(',') == 1 \
                and pos.index(',') != 0 and pos.index(',') != len(pos) - 1 \
                and int(pos.split(',')[0]) < int(dimensiones.split(',')[0])\
                and int(pos.split(',')[1]) < int(dimensiones.split(',')[1]):
            posiciones.append(pos + '\n')
        else:
            print('Debe ingresar una posición entera, positiva, menor a las',
                  'dimensiones y de la forma "x,y"')
        pos = input('Ingrese una posición prohibida o un 0 para terminar: ')
    tablero = open(nombre, 'x')
    tablero.write(dimensiones + '\n')
    tablero.writelines(posiciones)
    tablero.close()
    print('-------- tablero', nombre, 'creado correctamente --------')


def pos_valida(ficha):
    pos = input('Ingrese la posición inicial para ' + ficha.nombre + ': ')
    while not pos.replace(',', '', 1).isdigit() or pos.count(',') != 1 \
            or pos.index(',') == 0 or pos.index(',') == len(pos) - 1:
        print('Debe ingresar una posición positiva de la forma "x,y"')
        pos = input('Ingrese la posición inicial para ' + ficha.nombre + ': ')
    pos = (int(pos.split(',')[0]), int(pos.split(',')[1]))
    return pos


def opciones_tablero():
    print('\n(1) Imprimir el tablero con las fichas')
    print('(2) Preguntar por los movimientos de una pieza')
    print('(3) Verificar si se pueden mover las piezas' +
          ' sobre el tablero sin repetir posiciones')
    print('(0) Volver al menú principal')
    return input('Seleccione una opción: ')


def pedir_ficha(tablero):
    string = '\n'
    opciones = []
    for i in tablero.fichas:
        string += '(' + str(tablero.fichas.index(i) + 1) + ') ' + \
            i.nombre + '\n'
        opciones.append(str(tablero.fichas.index(i) + 1))
    while True:
        print(string[:-1])
        numero_ficha = input('Seleccione una pieza: ')
        if numero_ficha in opciones:
            break
        else:
            print('Ingrese una de las opciones entregadas')
    return int(numero_ficha)


def cargar_tablero():
    nombre = input('\nIngrese el nombre del archivo del tablero a usar: ')
    tablero = Tablero(nombre)
    ficha = input(
        'Ingrese el nombre del archivo de una ficha o un 0 para terminar: ')
    while ficha != '0':
        ficha = Ficha(ficha)
        pos = pos_valida(ficha)
        while True:
            pos_ocupada = False
            for i in tablero.fichas:
                if i.posicion == pos:
                    pos_ocupada = True
            if pos in tablero.prohibidas:
                print('Posición prohibida, no se puede ubicar ahí')
            elif pos_ocupada:
                print(
                    'Posición ocupada por otra ficha, no se puede ubicar ahí')
            elif pos[0] >= tablero.dimensiones[0] or \
                    pos[1] >= tablero.dimensiones[1]:
                print('Posición fuera del tablero, no se puede ubicar ahí')
            else:
                break
            pos = pos_valida(ficha)
        tablero.agregar_ficha(ficha, pos)
        ficha = input(
            'Ingrese el nombre del archivo una ficha o un 0 para terminar: ')
    while True:
        opcion = opciones_tablero()
        if opcion == '1':
            print(tablero)
        elif opcion == '2':
            numero = pedir_ficha(tablero)
            print(tablero.movimientos_posibles(numero))
        elif opcion == '3':
            output = input('\nIngrese el nombre del archivo de output: ')
            print('Procesando, esto puede tardar bastante...')
            if tablero.se_puede_recorrer(output):
                print('Se ha podido recorrer el tablero correctamente.',
                      'Resultado guardado en ' + output)
            else:
                print('Con las condiciones ingresadas, ',
                      'no se puede recorrer el tablero')
        elif opcion == '0':
            break
        else:
            print('\nIngrese una opción válida')


while True:
    opcion = opciones_inicio()
    if opcion == '1':
        crear_ficha()
    elif opcion == '2':
        crear_tablero()
    elif opcion == '3':
        cargar_tablero()
    elif opcion == '0':
        print('\nPrograma finalizado\n')
        break
    else:
        print('\nIngrese una opción válida')
