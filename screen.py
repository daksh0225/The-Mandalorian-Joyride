import os
import numpy
import random

class Screen:
    def __init__(self):
        self.__sky = '~'
        self.__ground = '_'
        self.__magnet = []
        # self.__beams = []
    
    def createGround(self, matrix, columns):
        for i in range(columns):
            matrix[40][i] = self.__ground

    def createSky(self, matrix, columns):
        for i in range(columns):
            matrix[0][i] = self.__sky
    
    def placeMagnets(self, matrix, columns):
        cnt = 0
        with open('./objects/magnet.txt') as mag:
            for line in mag:
                self.__magnet.append(line.strip('\n'))
                cnt = cnt+1
        m1 = random.randint(12,20)
        m2 = random.randint(1,7)
        b= random.randint(180,250)
        for i in range(len(self.__magnet)):
            # print(self.__magnet[i])
            for j in range(len(self.__magnet[i])):
                # print(self.__magnet[i][j], end='')
                matrix[i+m1][j+100] = self.__magnet[i][j]
                matrix[i+m2][j+b] = self.__magnet[i][j]