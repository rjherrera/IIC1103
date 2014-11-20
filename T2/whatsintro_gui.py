#!/usr/bin/python
#Filename: whatsintro_gui.py
# coding: utf8

import tkinter as tk
import random
from tkinter import font as tkFont
from tkinter import messagebox
from tkinter import ttk
import threading
import _thread
import time
import sys
import random
import queue


lastKeyPressed = None
isKeyPressed = False
app = None
def handler(event):
    app.actualiza_contador()

def esperar_click():
    return app.esperar_click()

def emisor(texto):
    return app.emisor(texto)

def mensaje_redactado():
    return app.mensaje_redactado()

def borrar_mensaje_redactado():
    return app.borrar_mensaje_redactado()

def agregar_mensaje_al_final(de,para,msg): 
    return app.agregar_mensaje_al_final(de,para,msg)

def agregar_mensaje_al_inicio(de,para,msg): 
    return app.agregar_mensaje_al_inicio(de,para,msg)

def borrar_lista_mensajes():
    return app.borrar_lista_mensajes()

class Application(tk.Tk):
    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()
        self.in_queue = queue.Queue()
        self.out_queue = queue.Queue()
        self.pollingTimeout = 250    
        self.midframe = None    
        self.base = None
        self.elementos = []
        global app
        app = self
        
    def initialize(self):
        self.grid()
        self.lastKeyPressed = None
        self.customFont = tkFont.Font(family="Helvetica")
        
        self.username = tk.StringVar()
        self.count = tk.StringVar()
        self.message = tk.StringVar()


        upperFrame = tk.Frame(self, relief = 'flat', borderwidth = 1)
        upperFrame.bind_all('<Key>',handler)
        upperFrame.pack()
        upperFrame.grid(column = 0, row = 0, columnspan = 3, sticky = 'news')
        
        self.username.set("@username:")
        usernameEntry = tk.Entry(upperFrame, textvariable = self.username, width = 30, state = 'readonly', relief = 'flat', font=self.customFont)
        usernameEntry.pack(side = 'left', padx = 5)

        messageFrame = tk.Frame(self, relief = 'flat', borderwidth = 1)
        #messageFrame.pack()
        messageFrame.grid(column = 0, row = 1, columnspan = 3, sticky = 'news')
        
        #messageEntry = tk.Text(messageFrame, textvariable = self.message, width = 30, relief = 'flat', font=self.customFont )
        self.messageEntry = tk.Text(messageFrame, width=60, height=3, borderwidth = 10, font=self.customFont, relief = 'flat')
        self.messageEntry.config(highlightbackground='black')
        self.messageEntry.pack(side = 'left')

        optionsFrame = tk.Frame(self, relief = 'flat', borderwidth = 1)
        #optionsFrame.pack()
        optionsFrame.grid(column = 0, row = 2, columnspan = 3, sticky = 'news')       
        #messageEntry = tk.Text(messageFrame, textvariable = self.message, width = 30, relief = 'flat', font=self.customFont )
        self.count.set("0 caracteres")
        countEntry = tk.Entry(optionsFrame, textvariable = self.count, width = 30, state = 'readonly', relief = 'flat', font=self.customFont)
        countEntry.pack(side = 'left')
        sendButton = tk.Button(optionsFrame,  text = 'Enviar', command = lambda:self.buttonClicked('enviar'), font = self.customFont)
        sendButton.pack(side = 'right')
        
        listFrame = tk.Frame(self, relief = 'flat', borderwidth = 1)
        #listFrame.pack()
        listFrame.grid(column = 0, row = 3, columnspan = 3, sticky = 'news') 
        cols = ('de', 'para', 'mensaje')
        cols_width = {'de':70,'para':70,'mensaje':250}
        self.tree = ttk.Treeview(listFrame,columns=cols, show="headings") 
        for each in cols:
            self.tree.heading(each,text=each.capitalize())
            self.tree.column(each,minwidth=cols_width[each],width=cols_width[each])
        
        
        self.tree.pack(expand=True, fill=tk.BOTH)
        
        buttosFrame = tk.Frame(self, relief = 'flat', borderwidth = 1)
        #buttosFrame.pack()
        buttosFrame.grid(column = 0, row = 4, columnspan = 3, sticky = 'news') 
        recibidosButton = tk.Button(buttosFrame, text = 'Recibidos', command = lambda:self.buttonClicked('recibidos'), font = self.customFont)
        enviadosButton = tk.Button(buttosFrame, text = 'Enviados', command = lambda:self.buttonClicked('enviados'), font = self.customFont)
        recibidosButton.pack(side = 'left')
        enviadosButton.pack(side = 'right')
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 1)
        lock = _thread.allocate_lock()
        self.condition = threading.Condition(lock)
        self.lastPressed = -1
        self.protocol("WM_DELETE_WINDOW", self.quit)
        self.isAlive = True
        
    
    def emisor(self, texto):
        self.username.set(str(texto))

    def mensaje_redactado(self):
        return self.messageEntry.get('1.0', 'end')

    def borrar_mensaje_redactado(self):
        self.messageEntry.delete('1.0', 'end')
        self.actualiza_contador()

    def agregar_mensaje_al_final(self, de, para, msg):
        e = self.tree.insert('', 'end', text='Widget Tour', values=(de,para,msg))
        self.elementos.append(e) 

    def agregar_mensaje_al_inicio(self, de, para, msg):
        e = self.tree.insert('', 0, text='Widget Tour', values=(de,para,msg)) 
        self.elementos.append(e)

    def actualiza_contador(self):
        caracteres=len(app.mensaje_redactado())-1
        self.count.set(str(caracteres)+" "+"caracteres")

    def borrar_lista_mensajes(self):
        for elemento in self.elementos:
            self.tree.delete(elemento)
        self.elementos = []

    def poll(self):
        if not self.in_queue.empty():
            try:
                tup = self.in_queue.get(False)
                if tup[0] == 'YesNo':
                    self.out_queue.put(tk.messagebox.askyesno(tup[1],tup[2]))
                elif tup[0] == 'Alert':
                    self.out_queue.put(tk.messagebox.showinfo(tup[1],tup[2]))
                elif tup[0] == 'Quit':
                    self.quit(False)   
            except Exception as e:
                print(e)
        self.after(self.pollingTimeout, self.poll)
        
    def quit(self, askConfirmation = True):
        if not askConfirmation or tk.messagebox.askyesno("Salir", "Seguro que quiere salir"):
            self.isAlive = False
            self.condition.acquire()
            self.condition.notify()
            self.condition.release()
            self.destroy()
            
    def terminar(self):
        self.enqueue(('Quit',))
            
    def start(self):
        t = threading.Thread(None, self.program, 'program', (self,))
        t.daemon = True
        t.start()
        self.after(self.pollingTimeout, self.poll)
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

    def esperar_presionar_tecla(self):
        global isKeyPressed
        lastKey = lastKeyPressed
        while isKeyPressed == False:
            pass
        isKeyPressed = False
        code = 0
        if len(lastKeyPressed) > 1:
            return lastKeyPressed
        else:
            return lastKeyPressed
        
        
    
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

    def dequeue(self, timeout = 1):
        try:
            result = self.out_queue.get(True, timeout)
            return result
        except:
            return False

    def aleatorio(self):
        return random.randint(1,3)
