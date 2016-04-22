# -*- coding: utf-8 -*-
import tkinter as tk

class tabuleiro:
    
    def __init__(self):        
        self.window = tk.Tk()
        self.window.geometry('300x330+850+50')
        self.window.rowconfigure(0, minsize = 100)
        self.window.rowconfigure(1, minsize = 100)
        self.window.rowconfigure(2, minsize = 100)
        self.window.rowconfigure(3, minsize = 100)
        self.window.columnconfigure(0, minsize = 100)
        self.window.columnconfigure(1, minsize = 100)
        self.window.columnconfigure(2, minsize = 100)
        
        self.botao_0x0 = tk.Button(self.window)
        self.botao_0x0.grid(row=0, column=0, sticky='nsew')
        
        self.botao_0x1 = tk.Button(self.window)
        self.botao_0x1.grid(row=0, column=1, sticky='nsew')
        
        self.botao_0x2 = tk.Button(self.window)
        self.botao_0x2.grid(row=0, column=2, sticky='nsew')
        
        self.botao_1x0 = tk.Button(self.window)
        self.botao_1x0.grid(row=1, column=0, sticky='nsew')
        
        self.botao_1x1 = tk.Button(self.window)
        self.botao_1x1.grid(row=1, column=1, sticky='nsew')
        
        self.botao_1x2 = tk.Button(self.window)
        self.botao_1x2.grid(row=1, column=2, sticky='nsew')
        
        self.botao_2x0 = tk.Button(self.window)
        self.botao_2x0.grid(row=2, column=0, sticky='nsew')
        
        self.botao_2x1 = tk.Button(self.window)
        self.botao_2x1.grid(row=2, column=1, sticky='nsew')
        
        self.botao_2x2 = tk.Button(self.window)
        self.botao_2x2.grid(row=2, column=2, sticky='nsew')
        
        self.label = tk.Label(self.window)
        self.label.grid(row=3,column=0,columnspan=3, sticky='nsew')
        
        
    def iniciar(self):
        self.window.mainloop()
    
    
        
app = tabuleiro()
app.iniciar()
        