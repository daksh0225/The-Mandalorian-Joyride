import os
from colorama import Fore, Back, Style
from screen import Obstacle
from board import Cell
import time
import config

class Bullet(Cell, Obstacle):
    def __init__(self):
        Cell.__init__(self)
        Obstacle.__init__(self)
        self._xpos = 0
        self._ypos = 0
    
    def destroy(self, matrix, x, y):
        for i in range(len(self._obs)):
            for j in range(len(self._obs[i])):
                # matrix[i+x][j+y]._char = ' '
                # matrix[i+x][j+y]._type = 'B'
                # matrix[i+x][j+y-1]._char = ' '
                # matrix[i+x][j+y-1]._type = 'B'
                if matrix[i+x][j+y-1]._type == 'B':
                    matrix[i+x][j+y-1]._char = ' '
                elif matrix[i+x][j+y-1]._type == 'S':
                    matrix[i+x][j+y-1]._char = 's'
                elif matrix[i+x][j+y-1]._type == 'C':
                    matrix[i+x][j+y-1]._char = '$'
                if matrix[i+x][j+y]._type == 'B':
                    matrix[i+x][j+y]._char = ' '
                elif matrix[i+x][j+y]._type == 'S':
                    matrix[i+x][j+y]._char = 's'
                elif matrix[i+x][j+y]._type == 'C':
                    matrix[i+x][j+y]._char = '$'

    def checkCollision(self, matrix, x, y):
        f1='y'
        f2='B'
        for i in range(len(self._obs)):
            for j in range(len(self._obs[i])):
                if matrix[i+x][j+y]._type == 'N':
                    config.collision(matrix, matrix[i+x][j+y]._xco, matrix[i+x][j+y]._yco, matrix[i+x][j+y]._len1, matrix[i+x][j+y]._len2, 'b')
                    f1=matrix[i+x][j+y]._char
                    f2='N'
                if matrix[i+x][j+y]._type == 'D':
                    config.collision(matrix, matrix[i+x][j+y]._xco, matrix[i+x][j+y]._yco, matrix[i+x][j+y]._len1, matrix[i+x][j+y]._len2, 'b')
                    f1=matrix[i+x][j+y]._char
                    f2='N'
                if matrix[i+x][j+y]._type == 'P':
                    config.collision(matrix, matrix[i+x][j+y]._xco, matrix[i+x][j+y]._yco, matrix[i+x][j+y]._len1, matrix[i+x][j+y]._len2, 'b')
                    f1=matrix[i+x][j+y]._char
                    f2='N'
                    # quit()
                elif matrix[i+x][j+y]._type == 'C':
                    f1='$'
                    f2='C'
                # elif matrix[i+x][j+y]._type == 'B' and (matrix[i+x][j+y]._char == '/' or matrix[i+x][j+y]._char == R"\""):
                #     print('bullet')
                #     f1='$'
                #     f2='N'
                elif matrix[i+x][j+y]._type == 'S':
                    f1='s'
                    f2='S'
        return f1, f2
                    
    def move(self, matrix, x, y):
        f,f1 = self.checkCollision(matrix, x, y)
        if f1 == 'N':
            return False
        else:
            for i in range(len(self._obs)):
                for j in range(len(self._obs[i])):
                    if j==1:
                        if matrix[i+x][j+y-2]._type == 'B':
                            matrix[i+x][j+y-2]._char = ' '
                        elif matrix[i+x][j+y-2]._type == 'S':
                            matrix[i+x][j+y-2]._char = 's'
                        elif matrix[i+x][j+y-2]._type == 'C':
                            matrix[i+x][j+y-2]._char = '$'
                    if f!='y':
                        matrix[i+x][j+y]._char = f
                    else:
                        matrix[i+x][j+y]._char = self._obs[i][j]
            return True
    def release(self, matrix, x, y):
        self._xpos = x
        self._ypos = y
        for i in range(130):
            time.sleep(0.01)
            self._ypos = self._ypos + 1
            f = self.move(matrix, self._xpos, self._ypos)
            if f == False:
                break
        self.destroy(matrix, self._xpos, self._ypos)
        return