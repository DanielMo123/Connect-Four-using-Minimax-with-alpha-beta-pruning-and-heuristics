#player1turn Morris
#Connect Four

import sys
import copy


def main():

    print("Welcome to connect four\nHow many columns is your board. Max 7")
    columns = int(input())

    while(columns > 7):
        print("Invalid number for rows\nEnter new number <=7")
        columns = int(input())
    
    print(columns)
    
    print("How many rows is your board. Max 6")
    rows = int(input())
    
    while(rows > 6):
        print("Invalid number for rows\nEnter new number <=6")
        rows = int(input())
        
    print(rows)
    
    print("How many colors in a row do you have to get?")

    requiredtowin = int(input())

    while(requiredtowin > 4 or requiredtowin < 3):
        print("Invalid number for required to win\nEnter new number")
        requiredtowin = int(input())

    print(requiredtowin)

    print("How much depth do you want to look for next best move")
    depth = int(input())

    while(depth > 10):
        print("Enter depth less than 10\nEnter new number")
        depth = int(input())

    print("Depths 7 and greater might take a while to calculate")

    board = [['0' for y in range(columns)] for x in range(rows)]

    player1turn = True


    while checkforwinner(board, columns, rows, requiredtowin) is False and isfull(board, columns, rows) is False:
            table = {}
            alphabeta(board, not player1turn, columns, rows, requiredtowin, table, depth)
##            print(len(table))
##            print(table)

            movesarray = []
            getmoves(board, not player1turn, columns, rows, movesarray)
            maxmove = -100000000000
            for item in movesarray:
                x = str(item)
                if x in table:
                    if table[x] > maxmove:
                        maxmove = table[x]
                        bestmove = x
                        b = item

            if player1turn == True:
                board = b
                printboard(board, columns, rows)
##                print(heuristic(board, columns, rows))

            else:
                insertcoin(board,  player1turn, columns, rows)

            player1turn = not player1turn

def alphabeta(board, player1turn, columns, rows, requiredtowin, table, depth):
    if str(board) in table:
        return table[str(board)]
    v = maxvalue(board, player1turn, columns, rows, requiredtowin, table, -100000000, 100000000, depth)
    return v

def maxvalue(board, player1turn, columns, rows, requiredtowin, table, alpha, beta, depth):   
    if str(board) in table:
        return table[str(board)]
    if checkforwinner(board, columns, rows, requiredtowin) is True and player1turn == True:
        table[str(board)] = 10000
        return 10000
    elif checkforwinner(board, columns, rows, requiredtowin) is True and player1turn == False:
        table[str(board)] = -10000
        return -10000
    elif isfull(board, columns, rows) is True:
        table[str(board)] = 0
        return 0
    elif depth == 0:
        table[str(board)] = heuristic(board, columns, rows)
        return heuristic(board, columns, rows)

    v = -100000000
    movesarray = []
    getmoves(board, player1turn, columns, rows, movesarray)
        
    for item in movesarray:
        v = max(v, minvalue(item, not player1turn, columns, rows, requiredtowin, table, alpha, beta, depth - 1))
        if v>= beta:
            table[str(board)] = v
##            print("hi")

            return v
    a = max(alpha, v)
    table[str(board)] = v
    return v

def minvalue(board, player1turn, columns, rows, requiredtowin, table, alpha, beta, depth):
    if str(board) in table:
        return table[str(board)]
    if checkforwinner(board, columns, rows, requiredtowin) is True and player1turn == True:
        table[str(board)] = 10000
        return 10000
    elif checkforwinner(board, columns, rows, requiredtowin) is True and player1turn == False:
        table[str(board)] = -10000
        return -10000
    elif isfull(board, columns, rows) is True:
        table[str(board)] = 0
        return 0
    elif depth == 0:
        table[str(board)] = heuristic(board, columns, rows)
        return heuristic(board, columns, rows)
    v = 100000000
    movesarray = []
    getmoves(board, player1turn, columns, rows, movesarray)    

    for item in movesarray:
        v = min(v, maxvalue(item, not player1turn, columns, rows, requiredtowin, table, alpha, beta, depth - 1))
        if v<= alpha:
            table[str(board)] = v
##            print("hi")

            return v
        
        beta = min(beta, v)
    table[str(board)] = v
    return v

def getmoves(board, player1turn, columns, rows, movesarray):
    if player1turn == True:
        for columnchoice in range(columns):
            state = copy.deepcopy(board)

            if board[0][columnchoice-1] == 'B' or board[0][columnchoice-1] == 'R':                   
                continue
            else:
                i = rows -1
                while(board[i][columnchoice-1] == 'B' or board[i][columnchoice-1] == 'R'):
                    i = i- 1          
                state[i][columnchoice-1] = 'R'
                movesarray.append(state)
    else:
        for columnchoice in range(columns):
            state = copy.deepcopy(board)

            if board[0][columnchoice-1] == 'B' or board[0][columnchoice-1] == 'R':                   
                continue
            else:
                i = rows -1
                while(board[i][columnchoice-1] == 'B' or board[i][columnchoice-1] == 'R'):
                    i = i- 1          
                state[i][columnchoice-1] = 'B'
                movesarray.append(state)
    return movesarray
 

def printboard(board, columns, rows):
    for x in range(rows):
        for y in range(columns):
            print(' %s |' % board[x][y], end='')
        print("\n")
        
def insertcoin(board, player1turn, columns, rows):
    if player1turn == True:
        print("In which column would player1 like to insert coin?")
        columnchoice = int(input())
        while board[0][columnchoice-1] == 'B' or board[0][columnchoice-1] == 'R':                   
            print("Can't put coin there. Enter new input: ")
            columnchoice = int(input())
        i = rows -1
        while(board[i][columnchoice-1] == 'B' or board[i][columnchoice-1] == 'R'):
            i = i- 1
        board[i][columnchoice-1] = 'B'
    else:
        print("In which column would player2 like to insert coin?")
        columnchoice = int(input())
        while(columnchoice <1 or columnchoice >columns):
            print("Can't put coin there. Enter new input: ")
            columnchoice = int(input())

        while board[0][columnchoice-1] == 'B' or board[0][columnchoice-1] == 'R':                   
            print("Can't put coin there. Enter new input: ")
            columnchoice = int(input())
        i = rows -1
        while(board[i][columnchoice-1] == 'B' or board[i][columnchoice-1] == 'R'):
            i = i- 1          
        board[i][columnchoice-1] = 'R'
          
def isfull(board, columns, rows):
    for x in range(rows):
        for y in range(columns):
            if board[x][y] == '0':
                return False
    return True

def checkforwinner(board, columns, rows, requiredtowin):
    if requiredtowin == 3:
        for x in range(rows):
            for y in range(columns):
                if y+2<columns:
                    if board[x][y] == 'B' and board[x][y+1] =='B' and board[x][y+2] == 'B':
##                        print("player1 won horizontal")
                        return True
                    if board[x][y] == 'R' and board[x][y+1] =='R' and board[x][y+2] == 'R':
##                        print("player2 won horizontal")
                        return True
        
        for x in range(rows):
            for y in range(columns):
                if x+2<rows:
                    if board[x][y] == 'B' and board[x+1][y] =='B' and board[x+2][y] == 'B':
##                        print("player1 won vertical")
                        return True
                    if board[x][y] == 'R' and board[x+1][y] =='R' and board[x+2][y] == 'R':
##                        print("player2 won vertical")
                        return True

        for x in range(rows):
            for y in range(columns):
                if x+2<rows and y-2>=0:
                    if board[x][y] == 'B' and board[x+1][y-1] =='B' and board[x+2][y-2] == 'B':
##                        print("player1 won with up horizontal")
                        return True
                    if board[x][y] == 'R' and board[x+1][y-1] =='R' and board[x+2][y-2] == 'R':
##                        print("player2 won with up horizontal")
                        return True
                  # down and over
        for x in range(rows):
            for y in range(columns):
                if y+2<columns and x+2<rows:
                    if board[x][y] == 'B' and board[x+1][y+1] =='B' and board[x+2][y+2] == 'B':
##                        print("player1 won with down horizontal")
                        return True
                    if board[x][y] == 'R' and board[x+1][y+1] =='R' and board[x+2][y+2] == 'R':
##                        print("player2 won with down horizontal")
                        return True
        return False
    else:
        for x in range(rows):
            for y in range(columns):
                if y+3<columns:
                    if board[x][y] == 'B' and board[x][y+1] =='B' and board[x][y+2] == 'B' and board[x][y+3] == 'B':
##                        print("player1 won horizontal")
                        return True
                    if board[x][y] == 'R' and board[x][y+1] =='R' and board[x][y+2] == 'R' and board[x][y+3] == 'R':
##                        print("player2 won horizontal")
                        return True
        
        for x in range(rows):
            for y in range(columns):
                if x+3<rows:
                    if board[x][y] == 'B' and board[x+1][y] =='B' and board[x+2][y] == 'B' and board[x+3][y] == 'B':
##                        print("player1 won vertical")
                        return True
                    if board[x][y] == 'R' and board[x+1][y] =='R' and board[x+2][y] == 'R' and board[x+3][y] == 'R':
##                        print("player2 won vertical")
                        return True

        for x in range(rows):
            for y in range(columns):
                if x+3<rows and y-3>=0:
                    if board[x][y] == 'B' and board[x+1][y-1] =='B' and board[x+2][y-2] == 'B' and board[x+3][y-3] == 'B':
##                        print("player1 won with up horizontal")
                        return True
                    if board[x][y] == 'R' and board[x+1][y-1] =='R' and board[x+2][y-2] == 'R' and board[x+3][y-3] == 'R':
##                        print("player2 won with up horizontal")
                        return True
                  
        for x in range(rows):
            for y in range(columns):
                if y+3<columns and x+3<rows:
                    if board[x][y] == 'B' and board[x+1][y+1] =='B' and board[x+2][y+2] == 'B' and board[x+3][y+3] == 'B':
##                        print("player1 won with down horizontal")
                        return True
                    if board[x][y] == 'R' and board[x+1][y+1] =='R' and board[x+2][y+2] == 'R' and board[x+3][y+3] == 'R':
##                        print("player2 won with down horizontal")
                        return True
        return False

def heuristic(board, columns, rows):
    z = 0
    for x in range(rows):
        for y in range(columns):
            if y+1<columns:
                if board[x][y] == 'B' and board[x][y+1] =='B':
                    z = z + 3
                if board[x][y] == 'R' and board[x][y+1] =='R':
                    z = z - 3
    
    for x in range(rows):
        for y in range(columns):
            if x+1<rows:
                if board[x][y] == 'B' and board[x+1][y] =='B':
                    z = z + 3
                if board[x][y] == 'R' and board[x+1][y] =='R':
                    z = z - 3

    for x in range(rows):
        for y in range(columns):
            if x+1<rows and y-1>=0:
                if board[x][y] == 'B' and board[x+1][y-1] =='B':
                    z = z + 3
                if board[x][y] == 'R' and board[x+1][y-1] =='R':
                    z = z - 3
    for x in range(rows):
        for y in range(columns):
            if y+1<columns and x+1<rows:

                if board[x][y] == 'B' and board[x+1][y+1] =='B':
                    z = z + 3
                if board[x][y] == 'R' and board[x+1][y+1] =='R':
                    z = z - 3
    for x in range(rows):
        for y in range(columns):
            if y+2<columns:
                if board[x][y] == 'B' and board[x][y+1] =='B' and board[x][y+2] == 'B':
                    z = z + 10
                if board[x][y] == 'R' and board[x][y+1] =='R' and board[x][y+2] == 'R':
                    z = z - 10
    
    for x in range(rows):
        for y in range(columns):
            if x+2<rows:
                if board[x][y] == 'B' and board[x+1][y] =='B' and board[x+2][y] == 'B':
                    z = z + 10
                if board[x][y] == 'R' and board[x+1][y] =='R' and board[x+2][y] == 'R':
                    z = z - 10

    for x in range(rows):
        for y in range(columns):
            if x+2<rows and y-2>=0:
                if board[x][y] == 'B' and board[x+1][y-1] =='B' and board[x+2][y-2] == 'B':
                    z = z + 10
                if board[x][y] == 'R' and board[x+1][y-1] =='R' and board[x+2][y-2] == 'R':
                    z = z - 10
    for x in range(rows):
        for y in range(columns):
            if y+2<columns and x+2<rows:
                if board[x][y] == 'B' and board[x+1][y+1] =='B' and board[x+2][y+2] == 'B':
                    z = z + 10
                if board[x][y] == 'R' and board[x+1][y+1] =='R' and board[x+2][y+2] == 'R':
                    z = z - 10
                    
    return z


main()



