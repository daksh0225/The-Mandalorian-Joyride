import os
import time
import signal
import numpy as numpy
from board import Board
from screen import Screen
from mando import Mando
from alarmexception import AlarmException
from getch import _getChUnix as getChar

def alarmhandler(signum, frame):
		''' input method '''
		raise AlarmException

def user_input(timeout=0.15):
    ''' input method '''
    signal.signal(signal.SIGALRM, alarmhandler)
    signal.setitimer(signal.ITIMER_REAL, timeout)
    
    try:
        text = getChar()()
        signal.alarm(0)
        return text
    except AlarmException:
        pass
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''

cnt = 0
screen = Screen()
board = Board(45, 300)
board.createBoard()
screen.createSky(board.matrix, board.columns)
screen.createGround(board.matrix, board.columns)
screen.placeMagnets(board.matrix, board.columns)
mando = Mando()
mando.loadMando(31, 5, board.matrix)
board.printBoard(cnt)
while True:
    # os.system('clear')
    # print("COINS:", 0, end = '\t \t')
    # print ("Lives of Boss Enemy:", 10, end='\t \t')
    # print("KILLS: ", 0)
    st = time.time()
    p = user_input()
    if p == 'q':
        quit()
    # print(p)
    end = time.time()
    diff = end -st
    if(diff> 0.1):
        cnt = cnt+1
        if(189+cnt<300):
            board.printBoard(cnt) 
        # else:

    
