coins = 0
bs = 0
lives = 10
shield_available = False
shield_active = False

def collision(matrix, x, y, l1, l2, flag):
    global bs, coins, lives, shield_active, shield_available
    # print(x)
    # print(y)
    # print(l1)
    # print(l2)
    # print('inside')
    # print(matrix[x][y]._type+'hello')
    if matrix[x][y]._type == 'C':
        if flag == 'm':
            coins = coins + 1
    elif matrix[x][y]._type == 'S':
        if flag == 'm':
            if(bs<3):
                bs = bs + 1
    elif matrix[x][y]._type == 'N':
        if flag == 'm':
            if shield_active == False:
                lives = lives - 1
            else:
                shield_active = False
                shield_available = False
        # print('gandu')
    for i in range(l1):
        for j in range(l2):
            matrix[i+x][j+y]._char = ' '
            matrix[i+x][j+y]._type = 'B'
            matrix[i+x][j+y]._xco = 0
            matrix[i+x][j+y]._yco = 0