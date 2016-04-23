# -*- coding: utf-8 -*-
import tkinter as tk
from jogo import jogo

class tabuleiro:
    
    def __init__(self):        
        self.window = tk.Tk()
        self.window.title("Jogo da Velha")
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
        self.botao_0x0.configure(command=self.clicar00)
        
        self.botao_0x1 = tk.Button(self.window)
        self.botao_0x1.grid(row=0, column=1, sticky='nsew')
        self.botao_0x1.configure(command=self.clicar01)
        
        self.botao_0x2 = tk.Button(self.window)
        self.botao_0x2.grid(row=0, column=2, sticky='nsew')
        self.botao_0x2.configure(command=self.clicar02)
        
        self.botao_1x0 = tk.Button(self.window)
        self.botao_1x0.grid(row=1, column=0, sticky='nsew')
        self.botao_1x0.configure(command=self.clicar10)
        
        self.botao_1x1 = tk.Button(self.window)
        self.botao_1x1.grid(row=1, column=1, sticky='nsew')
        self.botao_1x1.configure(command=self.clicar11)
        
        self.botao_1x2 = tk.Button(self.window)
        self.botao_1x2.grid(row=1, column=2, sticky='nsew')
        self.botao_1x2.configure(command=self.clicar12)
        
        self.botao_2x0 = tk.Button(self.window)
        self.botao_2x0.grid(row=2, column=0, sticky='nsew')
        self.botao_2x0.configure(command=self.clica20)
        
        self.botao_2x1 = tk.Button(self.window)
        self.botao_2x1.grid(row=2, column=1, sticky='nsew')
        self.botao_2x1.configure(command=self.clicar21)
        
        self.botao_2x2 = tk.Button(self.window)
        self.botao_2x2.grid(row=2, column=2, sticky='nsew')
        self.botao_2x2.configure(command=self.clicar22)
        
        self.label = tk.Label(self.window)
        self.label.grid(row=3,column=0,columnspan=3, sticky='nsew')
        self.label.configure(text="Vez: Jogador X")
        
        
        
    def iniciar(self):
        self.window.mainloop()
        
    def clicar00(self):
        if self.jogo.jogador == 1:
            self.botao_0x0.configure(fg='red', text='X')
            self.label.configure(text="Vez: Jogador O")
            self.jogo.recebe_jogada(0,0)
        else:
            self.botao_0x0.configure(fg='blue', text='O')
            self.label.configure(text="Vez: Jogador X")
            self.jogo.recebe_jogada(0,0)
        
        if self.jogo.limpa_jogadas:
            self.limpa_tela
        
    def clicar01(self):
        
    def clicar02(self):
        
    def clicar10(self):
        
    def clicar11(self):
    
    def clicar12(self):
        
    def clicar20(self):
        
    def clicar21(self):
        
    def clicar22(self):
    
    def limpa_tela(self):
        
    

        
    
    
        
app = tabuleiro()
app.iniciar()
        