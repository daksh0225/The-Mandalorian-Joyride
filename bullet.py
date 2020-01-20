import os
from colorama import Fore, Back, Style
from screen import Obstacle
from board import Cell
import time

class Bullet(Cell, Obstacle):
    def __init__(self):
        Cell.__init__(self)
        Obstacle.__init__(self)
        self._xpos = 0
        self._ypos = 0
    
    def move(self, matrix, x, y):
        for i in range(len(self._obs)):
            for j in range(len(self._obs[i])):
                matrix[i+x][j+y-2]._char = ' '
                matrix[i+x][j+y-2]._type = 'B'
                matrix[i+x][j+y]._char = self._obs[i][j]
                matrix[i+x][j+y]._type = 'F'
    def release(self, matrix, x, y):
        self._xpos = x
        self._ypos = y
        for i in range(130):
            time.sleep(0.01)
            self._ypos = self._ypos + 1
            self.move(matrix, self._xpos, self._ypos)