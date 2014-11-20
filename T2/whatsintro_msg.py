import http.client
import json

_ID = 0
_CLAVE = ""
_URL_BASE="intro.ing.puc.cl"
_PORT = 443
_URL_CONECTAR = "/conectar/"
_URL_RECIB_IDOS = "/mensaje_recibido/"
_URL_ENVIADOS = "/mensaje_enviado/"
_URL_ENVIAR = "/enviar_mensaje/"
_URL_VALIDAR = "/validar_encriptacion/"
_URL_CANTIDAD_ENVIADOS = "/cantidad_enviados/"
_URL_CANTIDAD_RECIBIDOS = "/cantidad_recibidos/"
_EMAIL = ""
_headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}

def conectar(email, clave):
    conn = http.client.HTTPConnection(_URL_BASE, _PORT)
    body = json.dumps({'email': email, 'clave': clave})
    conn.request("POST", _URL_CONECTAR,body)
    response = conn.getresponse()
    if(response.status == 200):
        global _EMAIL, _CLAVE
        _EMAIL = email
        _CLAVE = clave
        return True
    return False

def enviar_mensaje(mensaje_encriptado):
    conn = http.client.HTTPConnection(_URL_BASE, _PORT)
    body = json.dumps({'mensaje': mensaje_encriptado,'clave': _CLAVE, 'email':_EMAIL})
    conn.request("POST", _URL_ENVIAR,body)
    response = conn.getresponse()
    if response.status == 201:
        data = response.read().decode()
        mensaje = json.loads(data)
        return True, mensaje['log']
    if response.status == 500:
        data = response.read().decode()
        mensaje = json.loads(data)
        return False, mensaje['log'] 

def validar_encriptacion(mensaje, mensaje_encriptado):
    conn = http.client.HTTPConnection(_URL_BASE, _PORT)
    body = json.dumps({'mensaje': mensaje,'mensaje_encriptado': mensaje_encriptado, 'email':_EMAIL, 'clave':_CLAVE})
    conn.request("POST", _URL_VALIDAR,body)
    response = conn.getresponse()
    if response.status == 201:
        data = response.read().decode()
        respuesta = json.loads(data)
        return True, respuesta['log']
    if response.status == 500:
        data = response.read().decode()
        print(data)
        respuesta = json.loads(data)
        return False, respuesta['log'] 

def mensaje_enviado(k):
    conn = http.client.HTTPConnection(_URL_BASE, _PORT)
    body = json.dumps({'k': k,'clave': _CLAVE, 'email':_EMAIL})
    conn.request("POST", _URL_ENVIADOS, body)
    response = conn.getresponse()
    if(response.status == 200):
        data = response.read().decode()
        mensaje = json.loads(data)
        return mensaje['mensaje']

def mensaje_recibido(k):
    conn = http.client.HTTPConnection(_URL_BASE, _PORT)
    body = json.dumps({'k': k,'clave': _CLAVE, 'email':_EMAIL})
    conn.request("POST", _URL_RECIB_IDOS, body)
    response = conn.getresponse()
    if(response.status == 200):
        data = response.read().decode()
        mensaje = json.loads(data)
        return mensaje['mensaje']

def cantidad_recibidos():
    conn = http.client.HTTPConnection(_URL_BASE, _PORT)
    body = json.dumps({'clave': _CLAVE, 'email':_EMAIL})
    conn.request("POST", _URL_CANTIDAD_RECIBIDOS, body)
    response = conn.getresponse()
    if(response.status == 200):
        data = response.read().decode()
        respuesta = json.loads(data)
        return int(respuesta['cantidad'])

def cantidad_enviados():
    conn = http.client.HTTPConnection(_URL_BASE, _PORT)
    body = json.dumps({'clave': _CLAVE, 'email':_EMAIL})
    conn.request("POST", _URL_CANTIDAD_ENVIADOS, body)
    response = conn.getresponse()
    if(response.status == 200):
        data = response.read().decode()
        respuesta = json.loads(data)
        return int(respuesta['cantidad'])

def mensajes_enviados_hoy():
    conn = http.client.HTTPConnection(_URL_BASE, _PORT)
    conn.request("GET", _URL_ENVIADOS_HOY+str(_ID)+"/")
    response = conn.getresponse()
    if(response.status == 200):
        data = response.read().decode()
        mensajes = json.loads(data)
        return mensajes['cantidad']
    