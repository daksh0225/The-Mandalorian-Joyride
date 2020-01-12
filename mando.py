import os
import numpy

class Mando:
    def __init__(self):
        self.__mando = []

    def loadMando(self, x, y, matrix):
        with open('./objects/mando.txt') as man:
            for line in man:
                self.__mando.append(line.strip('\n'))
        for i in range(len(self.__mando)):
            for j in range(len(self.__mando[i])):
                matrix[i+x][j+y] = self.__mando[i][j]