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
from dragon import Dragon, dragonBullet
import random
import threading

def alarmhandler(signum, frame):
		''' input method '''
		raise AlarmException

def user_input(timeout=0.04):
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
board = Board(40, 200)
board.createBoard()
screen.createSky(board.matrix, board.columns)
screen.createGround(board.matrix, board.columns)
l1 = 0
# beam = Beam()
# beam.loadObstacle('beam')
# beamhead = Beam()
# beamhead.loadObstacle('beam_head')
# for j in range(10):
#     f = random.randint(0,2)
#     # if f == 1:
#     #     f=3
#     l = random.randint(6,10)
#     m1 = random.randint(2+l, 30-l)
#     m2 = random.randint(30+l1, 50+l1+10)
#     # m1 = 15
#     # m2 = 80
#     for i in range(l):
#         if f == 0:
#             if i == 0 or i == l-1:            
#                 beamhead.place(board.matrix, m1, m2, 0, i*2, l, 2*l)
#             else:
#                 beam.place(board.matrix, m1, m2, 0, i*2, l, 2*l)
#         elif f == 1:
#             if i == 0 or i == l-1:
#                 beamhead.place(board.matrix, m1, m2, i, i, l, l+1)
#             else:
#                 beam.place(board.matrix, m1, m2, i, i, l, l+1)
#         elif f == 2:
#             if i == 0 or i == l-1:
#                 beamhead.place(board.matrix, m1, m2, i, 0, l, 2)
#             else:
#                 beam.place(board.matrix, m1, m2, i, 0, l, 2)
#         elif f == 3:
#             if i == 0 or i == l-1:
#                 beamhead.place(board.matrix, m1, m2, i, -i, l, l+1)
#             else:
#                 beam.place(board.matrix, m1, m2, i, -i, l, l+1)
#     l1 = l+l1+20
# speed = Speed()
# speed.loadObstacle('speed_up')
# l1 = 0
# for i in range(5):
#     m1 = random.randint(1, 33)
#     m2 = random.randint(20+l1, 80+l1+10)
#     speed.place(board.matrix, m1, m2)
#     l1 = 5 + l1 +50
# coin = Coin()
# coin.loadObstacle('coin')
# for i in range(5):
#     c1 = random.randint(2,5)
#     c2 = random.randint(3,8)
#     x = random.randint(1,33)
#     y = random.randint(30, 260)
#     for j in range(c1):
#         for k in range(c2):
#             coin.place(board.matrix, x+j, y+k)
# coin.place(board.matrix, 23, 45)
# f = 0
# screen.placeMagnets(board.matrix, board.columns)
# screen.placePowerUps(board.matrix, board.columns)
mando = Mando()
mando.loadMando(board.matrix, 'n', cnt)
board.printBoard(cnt)
dragon = Dragon()
dragon.loadObstacle('dragon')
dragon.place(board.matrix, 20, 130)
st = time.time()
prev_gravity_time = time.time()
dBtime = time.time()
shield_time = time.time()
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
        print(mando.xpos)
        print(dragon.xpos)
        if mando.xpos < dragon.xpos and cnt+130 > 100:
            dragon.moveUp(board.matrix, mando.xpos, dragon.ypos)
            dragon.xpos = dragon.xpos - 1
        board.printBoard(cnt)
    elif p == 's':
        if mando.xpos < 32:
            mando.xpos = mando.xpos + 1
            mando.loadMando(board.matrix, 'd', cnt)
        print(mando.xpos)
        print(dragon.xpos)
        if cnt+130 > 100 and dragon.xpos < 20:
            dragon.moveDown(board.matrix, mando.xpos, dragon.ypos)
            dragon.xpos = dragon.xpos + 1
        board.printBoard(cnt)
    elif p == 'f':
        bullet = Bullet()
        bullet.loadObstacle('bullet')
        # bullet.move(board.matrix, mando.xpos+2, mando.ypos+6)
        t1 = threading.Thread(target = bullet.release, args = (board.matrix, mando.xpos+2, mando.ypos+6,), daemon=True)
        t1.start()
        # t1.join()
    elif p == ' ':
        if config.shield_available and config.shield_active == False:
            config.shield_active = True
            shield_time = time.time()
    end = time.time()
    diff = end -st
    if time.time() - shield_time > 15:
        config.shield_available = True
        shield_time = time.time()
    if time.time() - shield_time > 10:
        if config.shield_active:
            config.shield_available = False
            config.shield_active = False
            shield_time = time.time()
    if time.time() - dBtime > 1 and cnt + 130 > 100:
        dBullet = dragonBullet()
        dBullet.loadObstacle('dBullet')
        t1 = threading.Thread(target=dBullet.release, args = (board.matrix, mando.xpos+2, dragon.ypos - 1,), daemon=True)
        t1.start()
        dBtime = time.time()
    if time.time() - prev_gravity_time > 0.15:
        mando.gravity(board.matrix)
        if cnt+130 > 100 and dragon.xpos < 20:
            dragon.moveDown(board.matrix, mando.xpos, dragon.ypos)
            dragon.xpos = dragon.xpos + 1
        prev_gravity_time = time.time()
    if(diff> 0.15-config.bs*0.03):
        st = end
        # bullet.move(board.matrix, mando.xpos+2, mando.ypos+6)
        if cnt + 130 < 200:
            cnt = cnt+1
            mando.ypos = mando.ypos + 1
            mando.loadMando(board.matrix, 'r', cnt)
        # if cnt + 130 > 100:
        #     dragon.place(board.matrix, 20, 130)
        # if(cnt == mando.ypos):
        # if mando.ypos < 260:
        # if(130+cnt<300):
        if(config.lives <= 0):
            break
        board.printBoard(cnt)
    
