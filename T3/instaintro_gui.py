#!/usr/bin/python
# Filename: whatsintro_gui.py
# coding: utf8

import tkinter as tk
from tkinter import font as tkFont
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

import threading
import _thread
import time
import queue
import os
import glob

WIDTH, HEIGHT = 640, 480

lastKeyPressed = None
isKeyPressed = False
app = None


def handler(event):
    app.actualiza_contador()


def esperar_click():
    return app.esperar_click()


def obtener_pixeles():
    return app.obtener_pixels()


def actualizar_imagen(pixeles):
    return app.actualizar_pixels(pixeles)

def obtener_imagenes_mosaico():
    return app.imagenes

def salir():
    return app.quit()


class Application(tk.Tk):

    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()
        self.in_queue = queue.Queue()
        self.out_queue = queue.Queue()
        self.pollingTimeout = 1
        self.midframe = None
        self.base = None
        self.elementos = []
        self.pixeles = None
        global app
        app = self

    def initialize(self):
        self.grid()
        self.lastKeyPressed = None
        self.customFont = tkFont.Font(family="Helvetica")

        upperFrame = tk.Frame(self, relief='flat', borderwidth=1)
        upperFrame.pack()
        upperFrame.grid(column=0, row=0, columnspan=3, sticky='news')

        self.canvas_area = tk.Canvas(upperFrame, width=WIDTH, height=HEIGHT, bg="#000000")
        self.canvas_area.config(highlightbackground='black')
        self.canvas_area.pack()
        buttosFrame = tk.Frame(self, relief='flat', borderwidth=1)
        buttosFrame.grid(column=0, row=2, columnspan=3, sticky='news')
        filtro1_button = tk.Button(
            buttosFrame,
            text='Girar',
            command=lambda: self.buttonClicked('girar'),
            font=self.customFont)
        filtro2_button = tk.Button(
            buttosFrame,
            text='Gris',
            command=lambda: self.buttonClicked('gris'),
            font=self.customFont)
        filtro3_button = tk.Button(
            buttosFrame,
            text='Bordes',
            command=lambda: self.buttonClicked('bordes'),
            font=self.customFont)
        filtro4_button = tk.Button(
            buttosFrame,
            text='Mosaico',
            command=lambda: self.buttonClicked('mosaico'),
            font=self.customFont)
        filtro5_button = tk.Button(
            buttosFrame,
            text='Salir',
            command=lambda: self.buttonClicked('salir'),
            font=self.customFont)
        
        open_button = tk.Button(
            buttosFrame, text="Abrir", command=self.cargar_imagen, width=10)

        filtro1_button.grid(column=0, row=0,  sticky='news')
        filtro2_button.grid(column=1, row=0,  sticky='news')
        filtro3_button.grid(column=2, row=0,  sticky='news')
        filtro4_button.grid(column=3, row=0,  sticky='news')
        open_button.grid(column=7, row=0,  sticky='news')
        filtro5_button.grid(column=8, row=0,  sticky='news')

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        lock = _thread.allocate_lock()
        self.condition = threading.Condition(lock)
        self.lastPressed = -1
        self.protocol("WM_DELETE_WINDOW", self.quit)
        self.isAlive = True

    def cargar_imagen(self):
        fname = askopenfilename(
            filetypes=[("Image Files", "*.gif"),("GIF", '*.gif')])

        if fname:
            try:
                self.img = tk.PhotoImage(file=fname)
                self.canvas_area.create_image((WIDTH/2, HEIGHT/2), image=self.img, state="normal")  
                self.pixeles = self.procesar_pixels(self.img)
                self.imagenes = self.procesar_imagenes()
            except:
                print("Error",sys.exc_info()[0])
            return

    

    def procesar_pixels(self,img):
        self.pollingTimeout = 0
        print("procesando imagen\t\t\t\t\t\t", end=" ")
        if img == None:
            print('[No hay imagen abierta]')
            return None
            
        columnas = []
        width = img.width()
        height = img.height()
        for y in range(height):
            fila = []
            # print(x)
            for x in range(width):
                pixel_texto = img.get(x, y)
                if type(pixel_texto) is str:
                    pixel_partes = pixel_texto.split(' ')
                if type(pixel_texto) is tuple:
                    pixel_partes = pixel_texto
                pixel = (int(pixel_partes[0]), int(pixel_partes[1]), int(pixel_partes[2]))
                fila.append(pixel)
            columnas.append(fila)
        print('[OK]')
        self.pollingTimeout = 1
        return columnas

    def obtener_pixels(self):
        return self.pixeles

    def actualizar_pixels(self,pixeles):
        self.actualizar_negro()
        self.pixeles = pixeles
        self.actualizar_pixels_job()

    def actualizar_negro(self):
        #img = PhotoImage(width=300,height=300)
        data = ("{black}")
        self.img.put(data, to=(0,0,len(self.pixeles[0]),len(self.pixeles)))

    def actualizar_pixels_job(self):
        pixeles = self.pixeles
        self.pollingTimeout = 0
        print('actualizando pixeles de la imagen\t\t', end=" ")
        for i in range(len(pixeles)):
            row = ""
            for j in range(len(pixeles[i])):
                row += "#%02x%02x%02x" % pixeles[i][j]+" "
            row = "{"+row+"}"
            self.img.put(row, to=(0,i))
        print('[OK]')
        self.pollingTimeout = 1

    def procesar_imagenes(self):
        lista_imagenes = []
        files = glob.glob('mosaicos/*.gif')
        try:
            for fname in files:
                print(fname)
                img = tk.PhotoImage(file=fname)
                imagen = self.procesar_pixels(img)
                lista_imagenes.append(imagen)
            
        except:
                print("Error",sys.exc_info()[0])
        return lista_imagenes

    def poll(self):
        if not self.in_queue.empty():
            try:
                tup = self.in_queue.get(False)
                if tup[0] == 'YesNo':
                    self.out_queue.put(tk.messagebox.askyesno(tup[1], tup[2]))
                elif tup[0] == 'Alert':
                    self.out_queue.put(tk.messagebox.showinfo(tup[1], tup[2]))
                elif tup[0] == 'Quit':
                    self.quit(False)
            except Exception as e:
                print(e)
        self.after(self.pollingTimeout, self.poll)

    def quit(self, askConfirmation=True):
        if not askConfirmation or\
                tk.messagebox.askyesno("Salir", "Seguro que quiere salir"):
            self.isAlive = False
            self.condition.acquire()
            self.condition.notify()
            self.condition.release()
            self.destroy()

    def terminar(self):
        self.enqueue(('Quit',))

    def start(self):
        t = threading.Thread(None, self.program, (self,))
        t.daemon = True
        t.start()
        #self.after(self.pollingTimeout, self.poll)
        self.mainloop()
        print('Programa finalizado')

    def buttonClicked(self, btn):
        self.condition.acquire()
        self.lastPressed = btn
        self.condition.notify()
        self.condition.release()
        #print("click", self.lastPressed)

    def wait(self, t):
        time.sleep(t)

    def esperar_click(self):
        if not self.isAlive:
            return -1

        self.condition.acquire()
        self.condition.wait()
        btn = self.lastPressed
        self.condition.release()

        if self.isAlive:
            return btn
        else:
            return -1

    def loadProgram(self, program):
        self.program = program

    def mensaje(self, msg):
        self.messageVariable.set(msg)

    # comandos para manejar las colas
    def enqueue(self, commandTuple):
        try:
            self.in_queue.put(commandTuple, True, 1)
            return True
        except:
            return False

    def dequeue(self, timeout=1):
        try:
            result = self.out_queue.get(True, timeout)
            return result
        except:
            return False
