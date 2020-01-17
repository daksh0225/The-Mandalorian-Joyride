import os
import numpy
from colorama import Fore, Back, Style, init

init()

class Mando:
    def __init__(self):
        self.__mando = []
        self.xpos = 30
        self.ypos = 5
        with open('./objects/mandonew.txt') as man:
            for line in man:
                self.__mando.append(line.strip('\n'))

    def loadMando(self, matrix, flag, cnt):
        # self.__mando = []
        # print(len(self.__mando))
        if self.xpos > 0 and self.ypos > 0:
            for i in range(len(self.__mando)):
                for j in range(len(self.__mando[i])):
                    if flag == 'r' and j == 0 and self.ypos < 300:
                        matrix[i+self.xpos][j+self.ypos-1] = ' '
                    elif flag == 'l' and j == len(self.__mando[i])-1 and self.ypos > 0:
                        matrix[i+self.xpos][j+self.ypos+1] = ' '
                    elif flag == 'u' and i == len(self.__mando)-1 and self.xpos > 0:
                        matrix[i+self.xpos+1][j+self.ypos] = ' ' 
                    elif flag == 'd' and i == 0 and self.xpos < 30:
                        matrix[i+self.xpos-1][j+self.ypos] = ' ' 
                    matrix[i+self.xpos][j+self.ypos] = self.__mando[i][j]
    
    def gravity(self, matrix):
        if self.xpos<30 and self.xpos > 0 and self.ypos > 0:
            self.xpos = self.xpos + 1
            for i in range(len(self.__mando)):
                for j in range(len(self.__mando[i])):
                    if i == 0 :
                        matrix[i+self.xpos-1][j+self.ypos] = ' '
                    matrix[i+self.xpos][j+self.ypos] = self.__mando[i][j]