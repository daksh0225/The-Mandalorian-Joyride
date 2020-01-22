import os
from colorama import Fore, Back, Style
from screen import Obstacle
from board import Cell
import config
import time
# from bullet import Bullet


class dragonBullet(Cell, Obstacle):
    def __init__(self):
        Cell.__init__(self)
        Obstacle.__init__(self)
        self._xpos = 0
        self._ypos = 0
    
    def destroy(self, matrix, x, y):
        for i in range(len(self._obs)):
            for j in range(len(self._obs[i])):
                # matrix[i+x][y-j]._char = ' '
                # matrix[i+x][y-j]._type = 'B'
                # matrix[i+x][y-j-1]._char = ' '
                # matrix[i+x][y-j-1]._type = 'B'
                # if matrix[i+x][y-j-1]._type == 'B':
                #     matrix[i+x][y-j-1]._char = ' '
                # elif matrix[i+x][y-j-1]._type == 'S':
                #     matrix[i+x][y-j-1]._char = 's'
                # elif matrix[i+x][y-j-1]._type == 'C':
                #     matrix[i+x][y-j-1]._char = '$'
                if matrix[i+x][y-j]._type == 'B':
                    matrix[i+x][y-j]._char = ' '
                elif matrix[i+x][y-j]._type == 'S':
                    matrix[i+x][y-j]._char = 's'
                elif matrix[i+x][y-j]._type == 'C':
                    matrix[i+x][y-j]._char = '$'

    def checkCollision(self, matrix, x, y):
        f1='y'
        f2='B'
        for i in range(len(self._obs)):
            for j in range(len(self._obs[i])):
                if(matrix[i+x][y-j]._type == 'N') or matrix[i+x][y-j]._type == 'D':
                    config.collision(matrix, matrix[i+x][y-j]._xco, matrix[i+x][y-j]._yco, matrix[i+x][y-j]._len1, matrix[i+x][y-j]._len2, 'b')
                    f1=matrix[i+x][y-j]._char
                    f2='N'
                elif matrix[i+x][y-j]._type == 'C':
                    f1='$'
                    f2='C'
                elif matrix[i+x][y-j]._type == 'B' and matrix[i+x][y-j]._char == '>':
                    print('hello')
                    f1='$'
                    f2='M'
                elif matrix[i+x][y-j]._type == 'S':
                    f1='s'
                    f2='S'
        return f1, f2
                    
    def move(self, matrix, x, y):
        f,f1 = self.checkCollision(matrix, x, y)
        if f1 == 'M':
            return False
        else:
            for i in range(len(self._obs)):
                for j in range(len(self._obs[i])):
                    if j==len(self._obs[i])-1:
                        if matrix[i+x][y-j+len(self._obs[i])]._type == 'B':
                            matrix[i+x][y-j+len(self._obs[i])]._char = ' '
                        elif matrix[i+x][y-j+len(self._obs[i])]._type == 'S':
                            matrix[i+x][y-j+len(self._obs[i])]._char = 's'
                        elif matrix[i+x][y-j+len(self._obs[i])]._type == 'C':
                            matrix[i+x][y-j+len(self._obs[i])]._char = '$'
                    if f!='y':
                        matrix[i+x][y+j-len(self._obs[i])+1]._char = f
                    else:
                        matrix[i+x][y+j-len(self._obs[i])+1]._char = self._obs[i][j]
            return True
    def release(self, matrix, x, y):
        self._xpos = x
        self._ypos = y
        for i in range(50):
            time.sleep(0.03)
            self._ypos = self._ypos - 1
            f = self.move(matrix, self._xpos, self._ypos)
            if f == False:
                break
        self.destroy(matrix, self._xpos, self._ypos)
        return

class Dragon(Cell, Obstacle):
    def __init__(self):
        Obstacle.__init__(self)
        Cell.__init__(self)
        self.xpos = 0
        self.ypos = 0
        # Bullet.__init__(self)

    def place(self, matrix, x, y):
        # self._xco = x
        # self._yco = y
        self.xpos = x
        self.ypos = y
        for i in range(len(self._obs)):
            if i==0:
                max = len(self._obs[i])
            else:
                if len(self._obs[i]) > max:
                    max = len(self._obs[i])
            for j in range(len(self._obs[i])):
                if self._obs[i][j] != ' ':
                    matrix[i+x][j+y]._char = self._obs[i][j]
                    matrix[i+x][j+y]._xco = x
                    matrix[i+x][j+y]._yco = y
                    matrix[i+x][j+y]._type = 'D'
                    matrix[i+x][j+y]._len1 = len(self._obs)
                    matrix[i+x][j+y]._len2 = 68
    
    def moveUp(self, matrix, x, y):
        for i in range(len(self._obs)):
            for j in range(len(self._obs[i])):
                # if i == len(self._obs)-2:
                    # print(j)
                matrix[i+x+1][j+y]._char = ' '
                matrix[i+x+1][j+y]._type = 'B'
                matrix[i+x+1][j+y]._xco = 0
                matrix[i+x+1][j+y]._yco = 0
                matrix[i+x+1][j+y]._len1 = 0
                matrix[i+x+1][j+y]._len2 = 0

                matrix[i+x][j+y]._char = self._obs[i][j]
                matrix[i+x][j+y]._type = 'D'
                matrix[i+x][j+y]._xco = x
                matrix[i+x][j+y]._yco = y
                matrix[i+x][j+y]._len1 = len(self._obs)
                matrix[i+x][j+y]._len2 = 68
    
    def moveDown(self, matrix, x, y):
        for i in range(len(self._obs)):
            for j in range(len(self._obs[i])):
                # if i == 0:
                matrix[i+x-1][j+y]._char = ' '
                matrix[i+x-1][j+y]._type = 'B'
                matrix[i+x-1][j+y]._xco = 0
                matrix[i+x-1][j+y]._yco = 0
                matrix[i+x-1][j+y]._len1 = 0
                matrix[i+x-1][j+y]._len2 = 0

        for i in range(len(self._obs)):
            for j in range(len(self._obs[i])):
                matrix[i+x][j+y]._char = self._obs[i][j]
                matrix[i+x][j+y]._type = 'D'
                matrix[i+x][j+y]._xco = x
                matrix[i+x][j+y]._yco = y
                matrix[i+x][j+y]._len1 = len(self._obs)
                matrix[i+x][j+y]._len2 = 68