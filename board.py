import os
import numpy as np
from colorama import Fore, Back, Style, init
import config
init()

cellType = []
cellType = np.full((40, 300), 'B')

class Cell:
    def __init__(self):
        self._type = 'B'
        self._char = ' '
        self._xco = 0
        self._yco = 0
        self._len1 = 0
        self._len2 = 0

    # def display(self):
    #     print(self._char)

class Board:
    def __init__(self, rows, columns):
        # Cell.__init__(self)
        self.rows = rows
        self.columns = columns
        self.matrix = [[Cell() for j in range(self.columns)] for i in range(self.rows)]
        # self.__type = 'board'

    def createBoard(self):
        pass
        # self.matrix = np.full((self.rows, self.columns), Cell)
        # for i in range(self.rows):
        #     for j in range(self.columns):
        #         self.matrix[i].append(Cell())
        # for i in range(0, self.columns):
        #     self.matrix[0][i] = '~'
    
    def printBoard(self,cnt):
        # os.system('clear')
        print("\033[0;0H")
        print(Fore.RED + "LIVES LEFT:", str(config.lives)+' ', end = '\t \t' + Style.RESET_ALL)
        print(Fore.RED + "COINS:", config.coins, end = '\t \t' + Style.RESET_ALL)
        print (Fore.RED + "Lives of Boss Enemy:", 10, end='\t \t'+ Style.RESET_ALL)
        print(Fore.RED + "KILLS: ", 0 , end='\t \t'+ Style.RESET_ALL)
        print(Fore.RED + "Game Speed:",str(config.bs+1)+'x', end='\n'+ Style.RESET_ALL)
        for i in range(0, self.rows):
            for j in range(0+cnt ,130+cnt):
                if i==0:
                    print(Back.BLUE + self.matrix[i][j]._char + Style.RESET_ALL, end='')
                # elif self.matrix[i][j]._char == 'm':
                #     print(Back.RED + Fore.RED + self.matrix[i][j]._char + Style.RESET_ALL, end='')
                # elif self.matrix[i][j]._char == 't':
                #     print(Back.YELLOW + Fore.YELLOW + self.matrix[i][j]._char + Style.RESET_ALL, end='')
                # elif self.matrix[i][j]._char == 'v':
                #     print(Back.GREEN + Fore.GREEN + self.matrix[i][j]._char + Style.RESET_ALL, end='')
                # elif self.matrix[i][j]._char == 'c':
                #     print(Back.BLUE + Fore.BLUE + self.matrix[i][j]._char + Style.RESET_ALL, end='')
                # elif self.matrix[i][j]._char == 'p':
                #     print(Back.MAGENTA + Fore.MAGENTA + self.matrix[i][j]._char + Style.RESET_ALL, end='')
                # elif self.matrix[i][j]._char == 's':
                #     print(Back.YELLOW + Fore.RED + self.matrix[i][j]._char + Style.RESET_ALL, end='')
                # elif self.matrix[i][j]._char == 'x':
                #     print(Back.BLUE + Fore.BLUE + self.matrix[i][j]._char + Style.RESET_ALL, end='')
                elif self.matrix[i][j]._char == '$':
                    print(Fore.YELLOW + self.matrix[i][j]._char + Style.RESET_ALL, end='')
                # elif self.matrix[i][j]._char == '|':
                #     print(Back.RED + Fore.RED + self.matrix[i][j]._char + Style.RESET_ALL, end='')
                # elif self.matrix[i][j]._char == ' ':
                #    print(Back.YELLOW + Fore.YELLOW + self.matrix[i][j]._char + Style.RESET_ALL, end='')
                else:
        #             print(self.matrix[i][j]._char, end='')
                    print(self.matrix[i][j]._char, end = '')
            # print(Style.RESET_ALL)
            print()
    def changeType(self, type):
        self.__type = type
    
    def getType(self):
        return self.__type