# -*- coding: utf-8 -*-

import numpy as np


class jogo:
    
    def __init__(self):
        
        self.tabuleiro_jogo = np.zeros([3,3])  #tabuleiro do jogo, nao da interface
        
        self.jogador = 1                        #jogador atual. Quando 1 é X, quando 2 é O
        
        self.contador = 0
    
    def recebe_jogada(self, linha, coluna):
        self.tabuleiro_jogo[linha][coluna] = self.jogador #define a posição jogada e o jogador que a jogou
        if self.jogador == 1:
            self.jogador = 2
        else:
            self.jogador = 1
        self.contador += 1
    
    def verifica_ganhador(self):
         #casos para que X ganhe
        if self.tabuleiro_jogo[0][0] == 1 and self.tabuleiro_jogo[0][1] == 1 and self.tabuleiro_jogo[0][2] == 1:
            return 1
        elif self.tabuleiro_jogo[1][0] == 1 and self.tabuleiro_jogo[1][1] == 1 and self.tabuleiro_jogo[1][2] == 1:
            return 1
        elif self.tabuleiro_jogo[2][0] == 1 and self.tabuleiro_jogo[2][1] == 1 and self.tabuleiro_jogo[2][2] == 1:
            return 1
        elif self.tabuleiro_jogo[0][0] == 1 and self.tabuleiro_jogo[1][0] == 1 and self.tabuleiro_jogo[2][0] == 1:
            return 1
        elif self.tabuleiro_jogo[0][1] == 1 and self.tabuleiro_jogo[1][1] == 1 and self.tabuleiro_jogo[2][1] == 1:
            return 1
        elif self.tabuleiro_jogo[0][2] == 1 and self.tabuleiro_jogo[1][2] == 1 and self.tabuleiro_jogo[2][2] == 1:
            return 1
        elif self.tabuleiro_jogo[0][0] == 1 and self.tabuleiro_jogo[1][1] == 1 and self.tabuleiro_jogo[2][2] == 1:
            return 1
        elif self.tabuleiro_jogo[0][2] == 1 and self.tabuleiro_jogo[1][1] == 1 and self.tabuleiro_jogo[2][0] == 1:
            return 1
        
        #casos para que O ganhe
        elif self.tabuleiro_jogo[0][0] == 2 and self.tabuleiro_jogo[0][1] == 2 and self.tabuleiro_jogo[0][2] == 2:
            return 2
        elif self.tabuleiro_jogo[1][0] == 2 and self.tabuleiro_jogo[1][1] == 2 and self.tabuleiro_jogo[1][2] == 2:
            return 2
        elif self.tabuleiro_jogo[2][0] == 2 and self.tabuleiro_jogo[2][1] == 2 and self.tabuleiro_jogo[2][2] == 2:
            return 2
        elif self.tabuleiro_jogo[0][0] == 2 and self.tabuleiro_jogo[1][0] == 2 and self.tabuleiro_jogo[2][0] == 2:
            return 2
        elif self.tabuleiro_jogo[0][1] == 2 and self.tabuleiro_jogo[1][1] == 2 and self.tabuleiro_jogo[2][1] == 2:
            return 2
        elif self.tabuleiro_jogo[0][2] == 2 and self.tabuleiro_jogo[1][2] == 2 and self.tabuleiro_jogo[2][2] == 2:
            return 2
        elif self.tabuleiro_jogo[0][0] == 2 and self.tabuleiro_jogo[1][1] == 2 and self.tabuleiro_jogo[2][2] == 2:
            return 2
        elif self.tabuleiro_jogo[0][2] == 2 and self.tabuleiro_jogo[1][1] == 2 and self.tabuleiro_jogo[2][0] == 2:
            return 2
        
        #casos de empate
        elif self.contador == 9:
            return 0
        #caso contrário
        else:
            return -1
        
        
    def limpa_jogadas(self):
        if self.verifica_ganhador() == 1 or self.verifica_ganhador() == 2 or self.verifica_ganhador() == 0:
           self.tabuleiro_jogo = np.zeros([3,3])
           self.contador = 0
           return True
        else:
            return False
              