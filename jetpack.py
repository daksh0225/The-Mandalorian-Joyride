import os
import time
import signal
import numpy as numpy
from board import Board
from screen import Screen, Magnet, Obstacle
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

os.system('clear')
cnt = 0
screen = Screen()
board = Board(40, 300)
magnet = Magnet()
magnet.loadObstacle("magnet")
magnet.placeObstacle(10, 20, 50, 60, board.matrix)
board.createBoard()
screen.createSky(board.matrix, board.columns)
screen.createGround(board.matrix, board.columns)
screen.placeMagnets(board.matrix, board.columns)
screen.placePowerUps(board.matrix, board.columns)
mando = Mando()
mando.loadMando(board.matrix, 'n', cnt)
board.printBoard(cnt)
st = time.time()
while True:
    p = user_input()
    if p == 'q':
        quit()
    elif p == 'd':
        if mando.ypos < cnt + 125:
            mando.ypos = mando.ypos + 1
            mando.loadMando(board.matrix, 'r', cnt)
        board.printBoard(cnt)
    elif p == 'a':
        if mando.ypos > cnt + 1:
            mando.ypos = mando.ypos - 1
            mando.loadMando(board.matrix, 'l', cnt)
        board.printBoard(cnt)
    elif p == 'w':
        if mando.xpos > 1:
            mando.xpos = mando.xpos - 1
            mando.loadMando(board.matrix, 'u', cnt)
        board.printBoard(cnt)
    elif p == 's':
        if mando.xpos < 30:
            mando.xpos = mando.xpos + 1
            mando.loadMando(board.matrix, 'd', cnt)
        board.printBoard(cnt)
    end = time.time()
    diff = end -st
    if(diff> 0.15):
        st = end
        if cnt + 130 < 300:
            cnt = cnt+1
        if(cnt == mando.ypos):
            mando.ypos = mando.ypos + 1
            mando.loadMando(board.matrix, 'r', cnt)
        # if(130+cnt<300):
        mando.gravity(board.matrix)
        board.printBoard(cnt)
    
