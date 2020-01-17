import os
import numpy
import random
from colorama import Fore, Back, Style, init
init()

class Obstacle:
    def __init__(self):
        self.isCollided = False
        self.obs = []
        
    def loadObstacle(self, obstacle):
        print(obstacle)
        file = './objects/%s.txt' % obstacle
        with open(file) as obs:
            for line in obs:
                self.obs.append(line.strip('\n'))

class Magnet(Obstacle):
    def placeObstacle(self, x1, x2, y1, y2, matrix):
        m1 = random.randint(x1, x2)
        m2 = random.randint(y1, y2)
        for i in range(len(self.obs)):
            for j in range(len(self.obs[i])):
                print(i)
                print(j)
                print(m1)
                print(m2)
                matrix[i+m1][j+m2] = self.obs[i][j]

class Screen:
    def __init__(self):
        self.__sky = '~'
        self.__ground = '_'
        self.__magnet = []
        self.__shield = []
        self.__speed = []
    
    def createGround(self, matrix, columns):
        for i in range(columns):
            matrix[37][i] = self.__ground

    def createSky(self, matrix, columns):
        for i in range(columns):
            matrix[0][i] = self.__sky
    
    def placeMagnets(self, matrix, columns):
        with open('./objects/magnet.txt') as mag:
            for line in mag:
                self.__magnet.append(line.strip('\n'))
        m1 = random.randint(12,20)
        m2 = random.randint(1,7)
        b= random.randint(180,250)
        for i in range(len(self.__magnet)):
            for j in range(len(self.__magnet[i])):
                matrix[i+m1][j+100] = self.__magnet[i][j]
                matrix[i+m2][j+b] = self.__magnet[i][j]

    def placePowerUps(self, matrix, columns):
        with open('./objects/speed_up.txt') as speed:
            for line in speed:
                self.__speed.append(line.strip('\n'))
        for i in range(len(self.__speed)):
            for j in range(len(self.__speed[i])):
                matrix[i+30][j+40] = self.__speed[i][j]
                matrix[i+23][j+190] = self.__speed[i][j]
