import os
from colorama import Fore, Back, Style
from screen import Obstacle
from board import Cell

class Beam(Obstacle, Cell):
    def __init__(self):
        Cell.__init__(self)
        Obstacle.__init__(self)
    
    def place(self, matrix, x, y, f1, f2):
        # self._xco = x
        # self._yco = y
        for i in range(len(self._obs)):
            if i==0:
                max = len(self._obs[i])
            else:
                if len(self._obs[i]) > max:
                    max = len(self._obs[i])
            for j in range(len(self._obs[i])):
                matrix[i+x+f1][j+y+f2]._char = self._obs[i][j]
                matrix[i+x+f1][j+y+f2]._xco = x
                matrix[i+x+f1][j+y+f2]._yco = y
                matrix[i+x+f1][j+y+f2]._type = '|'
                matrix[i+x+f1][j+y+f2]._len1 = len(self._obs)
                matrix[i+x+f1][j+y+f2]._len2 = max