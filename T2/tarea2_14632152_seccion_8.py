import whatsintro_gui
import whatsintro_msg

def tarea(tablero):
    # Aqui empieza tu tarea
    clave = '874729149419666897'
    usuario = '@rjherrera'
    if whatsintro_msg.conectar(usuario, clave):
        whatsintro_gui.emisor(usuario)
    else:
        whatsintro_gui.messagebox.showinfo(title='Error de conexión', message='Falló la conexión con el servidor, verifique sus credenciales.',icon='warning')
        app.quit(False)
    while True:
        click = whatsintro_gui.esperar_click()
        if click == 'enviar':
            mensaje = whatsintro_gui.mensaje_redactado()[:-1]
            encriptado = encriptar(clave, mensaje)
            enviado = whatsintro_msg.enviar_mensaje(encriptado)
            if enviado[0]:
                whatsintro_gui.borrar_mensaje_redactado()
            else:
                whatsintro_gui.messagebox.showinfo(title='Error en el mensaje', message=enviado[1].capitalize(), icon='warning')
        elif click == 'recibidos':
            whatsintro_gui.borrar_lista_mensajes()
            for i in range(whatsintro_msg.cantidad_recibidos()):
                msje = whatsintro_msg.mensaje_recibido(i).split('\n')
                whatsintro_gui.agregar_mensaje_al_inicio(msje[0], msje[1], decriptar(clave, msje[2]))
        elif click == 'enviados':
            whatsintro_gui.borrar_lista_mensajes()
            for i in range(whatsintro_msg.cantidad_enviados()):
                msje = whatsintro_msg.mensaje_enviado(i).split('\n')
                whatsintro_gui.agregar_mensaje_al_inicio(msje[0], msje[1], decriptar(clave, msje[2]))


def cadena_inicio(clave, aleatoria=''.join(str(whatsintro_gui.random.randint(0, 9)) for i in range(10))):
    cadena = ''
    while len(cadena) < 256:
        cadena += clave + aleatoria
    cadena_inicio = list(int(i) for i in cadena[:256])
    return aleatoria, cadena_inicio


def lista_numeros(cadenainicio):
    numeros = list(range(256))
    for i in range(256):
        j = i + cadenainicio[i]
        if j > 255:
            j -= 256
        numeros[i], numeros[j] = numeros[j], numeros[i]
    return numeros


def binario(x):
    if isinstance(x, str):
        b = bin(ord(x))
    else:
        b = bin(x)
    return b[2:].zfill(8)


def binarizar(lista):
    return list(int(j) for j in (''.join(binario(i) for i in lista)))


def encriptar(clave, mensaje):
    aleatoria, inicio = cadena_inicio(clave)
    numeros = lista_numeros(inicio)
    codificado = ''
    for i, j in zip(binarizar(mensaje), binarizar(numeros)):
        if i == j:
            codificado += '0'
        else:
            codificado += '1'
    return aleatoria + codificado


def decriptar(clave, codificado):
    inicio = cadena_inicio(clave, codificado[:10])
    numeros = lista_numeros(inicio[1])
    binario = ''
    for i, j in zip(codificado[10:], binarizar(numeros)):
        if i == '0':
            binario += str(j)
        else:
            if j == 1:
                binario += '0'
            else:
                binario += '1'
    mensaje = ''
    while len(binario) > 0:
        mensaje += chr(int(binario[:8], 2))
        binario = binario[8:]
    return mensaje
    # Aqui termina tu tarea

app = whatsintro_gui.Application("tarea")
app.title('WhatsIntro')
app.loadProgram(tarea)
app.start()
