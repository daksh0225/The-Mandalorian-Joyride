import os
import numpy as np
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
        os.system('clear')
        print("COINS:", 0, end = '\t \t')
        print ("Lives of Boss Enemy:", 10, end='\t \t')
        print("KILLS: ", 0)
        for i in range(0, self.rows):
            for j in range(0+cnt ,189+cnt):
                print(self.matrix[i][j], end='')
            print()