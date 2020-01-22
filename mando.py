import os
import numpy
from colorama import Fore, Back, Style, init
from board import Board
import config

init()

# def config.collision(matrix, x, y, l1, l2):
#     # print(x)
#     # print(y)
#     # print(l1)
#     # print(l2)
#     # print('inside')
#     # print(matrix[x][y]._type+'hello')
#     if matrix[x][y]._type == 'C':
#         config.coins = config.coins + 1
#     elif matrix[x][y]._type == 'S':
#         if(config.bs<3):
#             config.bs = config.bs + 1
#     elif matrix[x][y]._type == 'N':
#         config.lives = config.lives - 1
#         # print('gandu')
#     for i in range(l1):
#         for j in range(l2):
#             matrix[i+x][j+y]._char = ' '
#             matrix[i+x][j+y]._type = 'B'
#             matrix[i+x][j+y]._xco = 0
#             matrix[i+x][j+y]._yco = 0

class Mando:
    def __init__(self):
        self.__mando = []
        self.xpos = 32
        self.ypos = 5
        with open('./objects/mandonew.txt') as man:
            for line in man:
                self.__mando.append(line.strip('\n'))

    def loadMando(self, matrix, flag, cnt):
        # self.__mando = []
        # print(len(self.__mando))
        self.checkCollision(matrix)
        if self.xpos > 0 and self.ypos > 0:
            for i in range(len(self.__mando)):
                for j in range(len(self.__mando[i])):
                    if flag == 'r' and j == 0 and self.ypos < 500:
                        if matrix[i+self.xpos][j+self.ypos-1]._type == 'P':
                            matrix[i+self.xpos][j+self.ypos-1]._char = 'M'
                        else:
                            matrix[i+self.xpos][j+self.ypos-1]._char = ' '
                            matrix[i+self.xpos][j+self.ypos-1]._type = 'B'
                    elif flag == 'l' and j == len(self.__mando[i])-1 and self.ypos > 0:
                        if matrix[i+self.xpos][j+self.ypos+1]._type == 'P':
                            matrix[i+self.xpos][j+self.ypos+1]._char = 'M'
                        else:
                            matrix[i+self.xpos][j+self.ypos+1]._char = ' '
                            matrix[i+self.xpos][j+self.ypos+1]._type = 'B'
                    elif flag == 'u' and i == len(self.__mando)-1 and self.xpos > 0:
                        if matrix[i+self.xpos+1][j+self.ypos]._type == 'P':
                            matrix[i+self.xpos+1][j+self.ypos]._char = 'M'
                        else:
                            matrix[i+self.xpos+1][j+self.ypos]._char = ' '
                            matrix[i+self.xpos+1][j+self.ypos]._type = 'B'
                    elif flag == 'd' and i == 0 and self.xpos < 33:
                        if matrix[i+self.xpos-1][j+self.ypos]._type == 'P':
                            matrix[i+self.xpos-1][j+self.ypos]._char == 'M'
                        else:
                            matrix[i+self.xpos-1][j+self.ypos]._char = ' '
                            matrix[i+self.xpos-1][j+self.ypos]._type = 'B'
                    matrix[i+self.xpos][j+self.ypos]._char = self.__mando[i][j]
                    if matrix[i+self.xpos][j+self.ypos]._type != 'P':
                        matrix[i+self.xpos][j+self.ypos]._type = 'M'
    
    def gravity(self, matrix):
        self.checkCollision(matrix)
        if self.xpos<32 and self.xpos > 0 and self.ypos > 0:
            self.xpos = self.xpos + 1
            for i in range(len(self.__mando)):
                for j in range(len(self.__mando[i])):
                    if i == 0 :
                        matrix[i+self.xpos-1][j+self.ypos]._char = ' '
                    matrix[i+self.xpos][j+self.ypos]._char = self.__mando[i][j]
        # if self.xpos > x1:
        #     print('a')
        #     if self.ypos > x2:
        #         print('b')
        #         self.loadMando(matrix, 'r', cnt)
        #         self.loadMando(matrix, 'u', cnt)
        #         self.loadMando(matrix, 'u', cnt)
        #     elif self.ypos < x2:
        #         print('c')
        #         self.loadMando(matrix, 'l', cnt)
        #         self.loadMando(matrix, 'u', cnt)
        #         self.loadMando(matrix, 'u', cnt)
        # elif self.xpos < x1:
        #     print('A')
        #     if self.ypos > x2:
        #         print('B')
        #         self.loadMando(matrix, 'r', cnt)
        #         self.loadMando(matrix, 'd', cnt)
        #     elif self.ypos < x2:
        #         print('C')
        #         self.loadMando(matrix, 'l', cnt)
        #         self.loadMando(matrix, 'd', cnt)

    def checkCollision(self, matrix):

        for i in range(len(self.__mando)):
            for j in range(len(self.__mando[i])):
                
                if matrix[i+self.xpos][j+self.ypos+1]._type == 'C':
                    print('hello1')
                    config.collision(matrix, matrix[i+self.xpos][j+self.ypos+1]._xco, matrix[i+self.xpos][j+self.ypos+1]._yco, matrix[i+self.xpos][j+self.ypos+1]._len1, matrix[i+self.xpos][j+self.ypos+1]._len2, 'm')
                elif matrix[i+self.xpos][j+self.ypos-1]._type == 'C':
                    print('hello1')
                    config.collision(matrix, matrix[i+self.xpos][j+self.ypos-1]._xco, matrix[i+self.xpos][j+self.ypos-1]._yco, matrix[i+self.xpos][j+self.ypos-1]._len1, matrix[i+self.xpos][j+self.ypos-1]._len2, 'm')
                elif matrix[i+self.xpos+1][j+self.ypos]._type == 'C':
                    print('hello1')
                    config.collision(matrix, matrix[i+self.xpos+1][j+self.ypos]._xco, matrix[i+self.xpos+1][j+self.ypos]._yco, matrix[i+self.xpos+1][j+self.ypos]._len1, matrix[i+self.xpos+1][j+self.ypos]._len2, 'm')
                elif matrix[i+self.xpos-1][j+self.ypos]._type == 'C':
                    print('hello1')
                    config.collision(matrix, matrix[i+self.xpos-1][j+self.ypos]._xco, matrix[i+self.xpos-1][j+self.ypos]._yco, matrix[i+self.xpos-1][j+self.ypos]._len1, matrix[i+self.xpos-1][j+self.ypos]._len2, 'm')
                elif matrix[i+self.xpos][j+self.ypos+1]._type == 'S':
                    print('hello1')
                    config.collision(matrix, matrix[i+self.xpos][j+self.ypos+1]._xco, matrix[i+self.xpos][j+self.ypos+1]._yco, matrix[i+self.xpos][j+self.ypos+1]._len1, matrix[i+self.xpos][j+self.ypos+1]._len2, 'm')
                elif matrix[i+self.xpos][j+self.ypos-1]._type == 'S':
                    print('hello1')
                    config.collision(matrix, matrix[i+self.xpos][j+self.ypos-1]._xco, matrix[i+self.xpos][j+self.ypos-1]._yco, matrix[i+self.xpos][j+self.ypos-1]._len1, matrix[i+self.xpos][j+self.ypos-1]._len2, 'm')
                elif matrix[i+self.xpos+1][j+self.ypos]._type == 'S':
                    print('hello1')
                    config.collision(matrix, matrix[i+self.xpos+1][j+self.ypos]._xco, matrix[i+self.xpos+1][j+self.ypos]._yco, matrix[i+self.xpos+1][j+self.ypos]._len1, matrix[i+self.xpos+1][j+self.ypos]._len2, 'm')
                elif matrix[i+self.xpos-1][j+self.ypos]._type == 'S':
                    print('hello1')
                    config.collision(matrix, matrix[i+self.xpos-1][j+self.ypos]._xco, matrix[i+self.xpos-1][j+self.ypos]._yco, matrix[i+self.xpos-1][j+self.ypos]._len1, matrix[i+self.xpos-1][j+self.ypos]._len2, 'm')
                elif matrix[i+self.xpos][j+self.ypos+1]._type == 'N':
                    print('hello1')
                    config.collision(matrix, matrix[i+self.xpos][j+self.ypos+1]._xco, matrix[i+self.xpos][j+self.ypos+1]._yco, matrix[i+self.xpos][j+self.ypos+1]._len1, matrix[i+self.xpos][j+self.ypos+1]._len2, 'm')
                elif matrix[i+self.xpos][j+self.ypos-1]._type == 'N':
                    print('hello1')
                    config.collision(matrix, matrix[i+self.xpos][j+self.ypos-1]._xco, matrix[i+self.xpos][j+self.ypos-1]._yco, matrix[i+self.xpos][j+self.ypos-1]._len1, matrix[i+self.xpos][j+self.ypos-1]._len2, 'm')
                elif matrix[i+self.xpos+1][j+self.ypos]._type == 'N':
                    print('hello1')
                    config.collision(matrix, matrix[i+self.xpos+1][j+self.ypos]._xco, matrix[i+self.xpos+1][j+self.ypos]._yco, matrix[i+self.xpos+1][j+self.ypos]._len1, matrix[i+self.xpos+1][j+self.ypos]._len2, 'm')
                elif matrix[i+self.xpos-1][j+self.ypos]._type == 'N':
                    print('hello1')
                    config.collision(matrix, matrix[i+self.xpos-1][j+self.ypos]._xco, matrix[i+self.xpos-1][j+self.ypos]._yco, matrix[i+self.xpos-1][j+self.ypos]._len1, matrix[i+self.xpos-1][j+self.ypos]._len2, 'm')
                # elif matrix[i+self.xpos][j+self.ypos+1]._type == 'D':
                #     print('hello1')
                #     config.collision(matrix, matrix[i+self.xpos][j+self.ypos+1]._xco, matrix[i+self.xpos][j+self.ypos+1]._yco, matrix[i+self.xpos][j+self.ypos+1]._len1, matrix[i+self.xpos][j+self.ypos+1]._len2, 'm')
                # elif matrix[i+self.xpos][j+self.ypos-1]._type == 'D':
                #     print('hello1')
                #     config.collision(matrix, matrix[i+self.xpos][j+self.ypos-1]._xco, matrix[i+self.xpos][j+self.ypos-1]._yco, matrix[i+self.xpos][j+self.ypos-1]._len1, matrix[i+self.xpos][j+self.ypos-1]._len2, 'm')
                # elif matrix[i+self.xpos+1][j+self.ypos]._type == 'D':
                #     print('hello1')
                #     config.collision(matrix, matrix[i+self.xpos+1][j+self.ypos]._xco, matrix[i+self.xpos+1][j+self.ypos]._yco, matrix[i+self.xpos+1][j+self.ypos]._len1, matrix[i+self.xpos+1][j+self.ypos]._len2, 'm')
                # elif matrix[i+self.xpos-1][j+self.ypos]._type == 'D':
                #     print('hello1')
                #     config.collision(matrix, matrix[i+self.xpos-1][j+self.ypos]._xco, matrix[i+self.xpos-1][j+self.ypos]._yco, matrix[i+self.xpos-1][j+self.ypos]._len1, matrix[i+self.xpos-1][j+self.ypos]._len2, 'm')