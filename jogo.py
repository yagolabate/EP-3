# -*- coding: utf-8 -*-

import numpy as np


class jogo:
    
    def __init__(self):
        
        self.tabuleiro_jogo = np.zeros([3,3])  #tabuleiro do jogo, nao da interface
        
        self.jogador = 1                        #jogador atual. Quando 1 é X, quando 2 é O
        
    
    def recebe_jogada(self, linha, coluna):
        self.tabuleiro_jogo[linha][coluna] = self.jogador #define a posição jogada e o jogador que a jogou
        if self.jogador == 1:
            self.jogador = 2
        else:
            self.jogador = 1
    
    def verifica_ganhador(self):
        
        
    def limpa_jogadas(self):
        if self.verifica_ganhador() == 1 or self.verifica_ganhador() == 2 or self.verifica_ganhador() == 0:
           self.tabuleiro_jogo = np.zeros([3,3])
           return True
        else:
            return False
              