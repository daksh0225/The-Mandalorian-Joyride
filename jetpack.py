import os
import time
import signal
import numpy as np
from board import Board
from screen import Screen, Obstacle
import config
from mando import Mando
from alarmexception import AlarmException
from getch import _getChUnix as getChar
from coins import Coin
from speed_up import Speed
from bullet import Bullet
from beam import Beam
import random
import threading

def alarmhandler(signum, frame):
		''' input method '''
		raise AlarmException

def user_input(timeout=0.05):
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
board.createBoard()
screen.createSky(board.matrix, board.columns)
screen.createGround(board.matrix, board.columns)
coin = Coin()
coin.loadObstacle('coin')
for i in range(5):
    c1 = random.randint(2,5)
    c2 = random.randint(3,8)
    x = random.randint(1,33)
    y = random.randint(30, 260)
    for j in range(c1):
        for k in range(c2):
            coin.place(board.matrix, x+j, y+k)
# coin.place(board.matrix, 23, 45)
l1 = 0
for j in range(7):
    f = random.randint(0,3)
    l = random.randint(11,15)
    print(f,l)
    beam = Beam()
    beam.loadObstacle('beam'+str(f)+str(l))
    m1 = random.randint(1+l, 36-l)
    m2 = random.randint(30+l1, 50+l1+10)
    beam.place(board.matrix, m1, m2)
    # for i in range(l):
    #     if f == 0:
    #         beam.place(board.matrix, m1, m2)
    #     elif f == 1:
    #         beam.place(board.matrix, m1, m2)
    #     elif f == 2:
    #         beam.place(board.matrix, m1, m2)
    #     elif f == 3:
    #         beam.place(board.matrix, m1, m2)
    l1 = l+20+l1
speed = Speed()
speed.loadObstacle('speed_up')
speed.place(board.matrix, 30, 90)
speed.place(board.matrix, 30, 105)
speed.place(board.matrix, 30, 120)
# f = 0
# screen.placeMagnets(board.matrix, board.columns)
# screen.placePowerUps(board.matrix, board.columns)
mando = Mando()
mando.loadMando(board.matrix, 'n', cnt)
bullet = Bullet()
board.printBoard(cnt)
st = time.time()
while True:
    p = user_input()
    if p == 'q':
        quit()
    elif p == 'd':
        # mando.checkCollision(board.matrix, 'r')
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
        if mando.xpos < 32:
            mando.xpos = mando.xpos + 1
            mando.loadMando(board.matrix, 'd', cnt)
        board.printBoard(cnt)
    elif p == 'f':
        bullet.loadObstacle('bullet')
        t1 = threading.Thread(target = bullet.release, args = (board.matrix, mando.xpos+2, mando.ypos+6,), daemon=True)
        t1.start()
        # t1.join()
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
    
