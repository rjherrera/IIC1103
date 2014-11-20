#!/usr/bin/python
#Filename: pokerGUI.py
# coding: utf8

import tkinter as tk
import random
from tkinter import font as tkFont
from tkinter import messagebox
import threading
import _thread
import time
import sys
import random
import queue


lastKeyPressed = None
isKeyPressed = False
def handler(event):
    global lastKeyPressed, isKeyPressed
    if event.keysym == 'Right':
        lastKeyPressed = 'derecha'
    elif event.keysym == 'Left':
        lastKeyPressed = 'izquierda'
    elif event.keysym == 'Up':
        lastKeyPressed = 'arriba'
    elif event.keysym == 'Down':
        lastKeyPressed = 'abajo'
    else:
        lastKeyPressed = event.char
    isKeyPressed = True
    
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
        
    def initialize(self):
        self.grid()
        self.lastKeyPressed = None
        self.customFont = tkFont.Font(family="Helvetica", size=40)
        upperFrame = tk.Frame(self, relief = 'flat', borderwidth = 1)
        upperFrame.bind_all('<Key>',handler)
        upperFrame.pack()
        upperFrame.grid(column = 0, row = 0, columnspan = 3, sticky = 'news')
        self.betVariable = tk.StringVar()
        
        betEntry = tk.Entry(upperFrame, textvariable = '', width = 2,state = 'readonly', relief = 'flat')
        betEntry.pack(side = 'left')
        self.creditsVariable = tk.StringVar()
        self.creditsVariable.set(0)
        creditsEntry = tk.Entry(upperFrame, textvariable = self.creditsVariable, width = 5,
                                state = 'readonly', relief = 'flat', font=self.customFont)
        creditsEntry.pack(side = 'right', padx = 5)
        label3 = tk.Label(upperFrame, text = 'Puntaje:', anchor = 'nw', font=self.customFont)
        label3.pack(side = 'right')
        #label3.grid(column = 2, row = 0, sticky = 'e', padx = 50)
        
        self.messageVariable = tk.StringVar()
        label2 = tk.Label(upperFrame, textvariable = self.messageVariable)
        label2.pack(fill = 'x')
        self.midframe = tk.Frame(self, relief='ridge', borderwidth=1)
        self.midframe.grid(column = 0, row = 1, columnspan = 3, sticky = 'news')
        self.midframe.grid()
        self.midframe.grid_rowconfigure(0, weight = 1)
        #self.base = tk.PhotoImage(file = 'blanco.gif')
        self.buttons = [None] * 16
        letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
        for i in range(0,16):
            self.midframe.grid_columnconfigure(i, weight = 1)
            frame = tk.Frame(self.midframe, relief = 'ridge', borderwidth = 1, width=140, height=150)
            #frame.pack()
            frame.pack_propagate(0)
            frame.grid(column = (i)%4, row = (i)//4, sticky = 'news')
            self.buttons[i] =  tk.StringVar()
            myvar = tk.Entry(frame, textvariable = self.buttons[i], width = 5, state = 'readonly', relief = 'flat', font=self.customFont)
            myvar.config(justify='center')
            myvar.pack(side = 'left')
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 1)
        lock = _thread.allocate_lock()
        self.condition = threading.Condition(lock)
        self.lastPressed = -1
        self.protocol("WM_DELETE_WINDOW", self.quit)
        self.isAlive = True
        
    def inicia_juego(self):
        a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p = (0,)*16
        lista = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        lista_aleatoria = []
        index = 9
        while index > 0  :
            al = random.randint(0,len(lista)-1)
            el = lista.pop(al)
            lista_aleatoria.append(el)
            index-=1
        if 0 in lista_aleatoria: a = self.aleatorio()
        if 1 in lista_aleatoria: b = self.aleatorio()
        if 2 in lista_aleatoria: c = self.aleatorio()
        if 3 in lista_aleatoria: d = self.aleatorio()
        if 4 in lista_aleatoria: e = self.aleatorio()
        if 5 in lista_aleatoria: f = self.aleatorio()
        if 6 in lista_aleatoria: g = self.aleatorio()
        if 7 in lista_aleatoria: h = self.aleatorio()
        if 8 in lista_aleatoria: i = self.aleatorio()
        if 9 in lista_aleatoria: j = self.aleatorio()
        if 10 in lista_aleatoria: k = self.aleatorio()
        if 11 in lista_aleatoria: l = self.aleatorio()
        if 12 in lista_aleatoria: m = self.aleatorio()
        if 13 in lista_aleatoria: n = self.aleatorio()
        if 14 in lista_aleatoria: o = self.aleatorio()
        if 15 in lista_aleatoria: p = self.aleatorio()
        return a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p
        
    def update(self,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p, puntaje):
        self.creditsVariable.set(str(puntaje))
        lista = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p]
        for index in range(0,len(lista)):
            if lista[index] != 0  :
                self.buttons[index].set(lista[index])
            else:
                self.buttons[index].set("")
              
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

    def wait(self, t):
        time.sleep(t)
        
    def esperarClick(self):
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

    def esperarPresionarTecla(self):
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

    def cambiarCredito(self, credits):
        self.creditsVariable.set(credits)

    
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
