import os
import numpy as np
from colorama import Fore, Back, Style, init

init()
class Board:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = []
    
    def createBoard(self):
        self.matrix = np.full((self.rows, self.columns), ' ')
        # for i in range(0, self.columns):
        #     self.matrix[0][i] = '~'
    
    def printBoard(self,cnt):
        # os.system('clear')
        print("\033[0;0H")
        print(Fore.RED + "COINS:", 0, end = '\t \t' + Style.RESET_ALL)
        print (Fore.RED + "Lives of Boss Enemy:", 10, end='\t \t'+ Style.RESET_ALL)
        print(Fore.RED + "KILLS: ", 0 , end='\n'+ Style.RESET_ALL)
        for i in range(0, self.rows):
            for j in range(0+cnt ,130+cnt):
                if i==0:
                    print(Back.BLUE + self.matrix[i][j] + Style.RESET_ALL, end='')
                elif self.matrix[i][j] == 'm':
                    print(Back.RED + Fore.RED + self.matrix[i][j] + Style.RESET_ALL, end='')
                elif self.matrix[i][j] == 't':
                    print(Back.YELLOW + Fore.YELLOW + self.matrix[i][j] + Style.RESET_ALL, end='')
                elif self.matrix[i][j] == 'v':
                    print(Back.GREEN + Fore.GREEN + self.matrix[i][j] + Style.RESET_ALL, end='')
                elif self.matrix[i][j] == 'c':
                    print(Back.BLUE + Fore.BLUE + self.matrix[i][j] + Style.RESET_ALL, end='')
                elif self.matrix[i][j] == 'p':
                    print(Back.MAGENTA + Fore.MAGENTA + self.matrix[i][j] + Style.RESET_ALL, end='')
                elif self.matrix[i][j] == 's':
                    print(Fore.RED + self.matrix[i][j] + Style.RESET_ALL, end='')
                elif self.matrix[i][j] == 'x':
                    print(Back.BLUE + Fore.BLUE + self.matrix[i][j] + Style.RESET_ALL, end='')
                # elif self.matrix[i][j] == '':
                #     print(Back.MAGENTA + Fore.MAGENTA + self.matrix[i][j] + Style.RESET_ALL, end='')
                else:
                    print(self.matrix[i][j], end='')
                # print(Style.RESET_ALL)
            print()