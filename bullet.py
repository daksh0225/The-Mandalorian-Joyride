import os
from colorama import Fore, Back, Style
from screen import Obstacle
from board import Cell
import time
import config

class Bullet(Cell, Obstacle):
    # def __init__(self):
    #     Cell.__init__(self)
    #     Obstacle.__init__(self)
    #     self._xpos = 0
    #     self._ypos = 0
    
    # def destroy(self, matrix, x, y):
    #     for i in range(len(self._obs)):
    #         for j in range(len(self._obs[i])):
    #             # matrix[i+x][j+y]._char = ' '
    #             # matrix[i+x][j+y]._type = 'B'
    #             # matrix[i+x][j+y-1]._char = ' '
    #             # matrix[i+x][j+y-1]._type = 'B'
    #             if matrix[i+x][j+y-1]._type == 'B':
    #                 matrix[i+x][j+y-1]._char = ' '
    #             elif matrix[i+x][j+y-1]._type == 'S':
    #                 matrix[i+x][j+y-1]._char = 's'
    #             elif matrix[i+x][j+y-1]._type == 'C':
    #                 matrix[i+x][j+y-1]._char = '$'
    #             if matrix[i+x][j+y]._type == 'B':
    #                 matrix[i+x][j+y]._char = ' '
    #             elif matrix[i+x][j+y]._type == 'S':
    #                 matrix[i+x][j+y]._char = 's'
    #             elif matrix[i+x][j+y]._type == 'C':
    #                 matrix[i+x][j+y]._char = '$'

    # def checkCollision(self, matrix, x, y):
    #     f1='y'
    #     f2='B'
    #     # print(x)
    #     # print(y)
    #     for i in range(len(self._obs)):
    #         for j in range(len(self._obs[i])):
    #             if matrix[i+x][j+y]._type == 'N':
    #                 config.collision(matrix, matrix[i+x][j+y]._xco, matrix[i+x][j+y]._yco, matrix[i+x][j+y]._len1, matrix[i+x][j+y]._len2, 'b')
    #                 f1=matrix[i+x][j+y]._char
    #                 f2='N'
    #             if matrix[i+x][j+y]._type == 'D':
    #                 config.collision(matrix, matrix[i+x][j+y]._xco, matrix[i+x][j+y]._yco, matrix[i+x][j+y]._len1, matrix[i+x][j+y]._len2, 'b')
    #                 f1=matrix[i+x][j+y]._char
    #                 f2='N'
    #             if matrix[i+x][j+y]._type == 'P':
    #                 config.collision(matrix, matrix[i+x][j+y]._xco, matrix[i+x][j+y]._yco, matrix[i+x][j+y]._len1, matrix[i+x][j+y]._len2, 'b')
    #                 f1=matrix[i+x][j+y]._char
    #                 f2='N'
    #                 # quit()
    #             elif matrix[i+x][j+y]._type == 'C':
    #                 f1='$'
    #                 f2='C'
    #             # elif matrix[i+x][j+y]._type == 'B' and (matrix[i+x][j+y]._char == '/' or matrix[i+x][j+y]._char == R"\""):
    #             #     print('bullet')
    #             #     f1='$'
    #             #     f2='N'
    #             elif matrix[i+x][j+y]._type == 'S':
    #                 f1='s'
    #                 f2='S'
    #     return f1, f2
                    
    # def move(self, matrix, x, y):
    #     f,f1 = self.checkCollision(matrix, x, y)
    #     if f1 == 'N':
    #         return False
    #     else:
    #         for i in range(len(self._obs)):
    #             for j in range(len(self._obs[i])):
    #                 if j==1:
    #                     if matrix[i+x][j+y-2]._type == 'B':
    #                         matrix[i+x][j+y-2]._char = ' '
    #                     elif matrix[i+x][j+y-2]._type == 'S':
    #                         matrix[i+x][j+y-2]._char = 's'
    #                     elif matrix[i+x][j+y-2]._type == 'C':
    #                         matrix[i+x][j+y-2]._char = '$'
    #                 if f!='y':
    #                     matrix[i+x][j+y]._char = f
    #                 else:
    #                     matrix[i+x][j+y]._char = self._obs[i][j]
    #         return True
    # def release(self, matrix, x, y, cnt):
    #     self._xpos = x
    #     self._ypos = y
    #     # print(x)
    #     # print(y)
    #     print()
    #     for i in range(min(130, (330-cnt))):
    #         time.sleep(0.01)
    #         self._ypos = self._ypos + 1
    #         f = self.move(matrix, self._xpos, self._ypos)
    #         if f == False:
    #             break
    #     self.destroy(matrix, self._xpos, self._ypos)
    #     return
    def __init__(self, x, y):
        self.__my_co = {
            x : [y, y + 1]
        }
        self.__my_print = {
            0 : ['-', '>']
        }
        self.__living = 1
    def move(self, matrix, last):
        if self.__living == 0:
            return
        for i in self.__my_co:
            for j in self.__my_co[i]:
                if matrix[i][j]._type != 'C' and matrix[i][j]._type != 'S':
                    matrix[i][j]._char = ' '
                    matrix[i][j]._type = 'B'
       
        new_co = {}
        for i in self.__my_co:
            new_co[i] = []
            for j in self.__my_co[i]:
                new_co[i].append(j + 4)
                for k in range(j, j + 5):
                    if matrix[i][k]._type == 'N':
                        config.collision(matrix, matrix[i][k]._xco, matrix[i][k]._yco, matrix[i][k]._len1, matrix[i][k]._len2, 'b')
                        self.__living = 0
                        return
                    elif matrix[i][k]._type == 'D':
                        config.collision(matrix, i, k, matrix[i][k]._len1, matrix[i][k]._len2, 'b')
                        self.__living = 0
                        return
        for i in new_co:
            for j in new_co[i]:
                if j >= last:
                    self.__living = 0
                    return
         
        self.__my_co = new_co
        l = 0
        m = 0
        for i in self.__my_co:
            m = 0
            for j in self.__my_co[i]:
                if matrix[i][j]._type != 'C' and matrix[i][j]._type != 'S':
                    matrix[i][j]._char = self.__my_print[l][m]
                m += 1
            l += 1
        return