__author__ = 'joao'

from random import randint, seed

##Ta funcional porém o "bot" nao ta funcionando bem

def verifyWinnier(game):
    player1_row = 0
    player2_row = 0
    player1_column = 0
    player2_column= 0

    if (game[0][0] == 1) and (game[1][1] == 1) and (game[2][2] == 1):
        print("Player 1 won!")
        printGame(game)
        return True

    if (game[0][0] == 2) and (game[1][1] == 2) and (game[2][2] == 2):
        print("Player 2 won!")
        printGame(game)
        return True

    if (game[0][2] == 1) and (game[1][1] == 1) and (game[2][0] == 1):
        print("Player 1 won!")
        printGame(game)
        return True

    if (game[0][2] == 2) and (game[1][1] == 2) and (game[2][0] == 2):
        print("Player 2 won!")
        printGame(game)
        return True  

    for i in range(0,3):
        for j in range(0,3):
            if game[j][i] == 1: player1_row += 1
            elif game[j][i] == 2: player2_row += 1
            if player1_row == 3: 
                print("Player 1 won!")
                printGame(game)
                return True
            elif player2_row == 3:
                print("Player 2 won!")
                printGame(game)
                return True
                
            if game[i][j] == 1: player1_column += 1
            elif game[i][j] == 2: player2_column += 1
            if player1_column == 3:
                print("Player 1 won!")
                printGame(game)
                return True
            elif player2_column == 3:
                print("Player 2 won!")
                printGame(game)
                return True

        for i in range(0,3):
            if game[0][i] == 0: break
            elif game[1][i] == 0: break
            elif game[2][i] == 0: break
            elif i == 2: 
                print("Thats a tie!")
                printGame(game)
                return True

        player1_row = 0
        player2_row = 0
        player1_column = 0
        player2_column= 0

    return False

def printGame(game):
    for row in range(0,3):
        for column in range(0,3):
            print(str(game[row][column]) + " ", end = '')
        print()

def checkPriority(i,j,priority,game):
    for index in range(0,3):
        if game[i][index] == 1: priority[i][j] += 1
        if game[index][j] == 1: priority[i][j] += 1
    
    if (i == 0 and j == 0) or (i == 1 and j == 1) or (i == 2 and j == 2):
        if game[0][0] == 1: priority[i][j] += 1
        if game[1][1] == 1: priority[i][j] += 1
        if game[2][2] == 1: priority[i][j] += 1

    if (i == 0 and j == 2) or (i == 1 and j == 1) or (i == 2 and j == 0):
        if game[0][2] == 1: priority[i][j] += 1
        if game[1][1] == 1: priority[i][j] += 1
        if game[2][0] == 1: priority[i][j] += 1

def computerTurn(game, turn):
    priority = [[0,0,0],
                [0,0,0],
                [0,0,0]]
    
    if turn == 1:
        while True:
            row = randint(0,2)
            column = randint(0,2)
            if game[row][column] == 0:
                game[row][column] = 2 
                break
        return game

    for row in range(0,3):
        for column in range(0,3):
            print(str(priority[row][column]) + " ", end = '')
        print()

    for i in range(0,3):
        for j in range(0,3):
            if game[i][j] == 0: checkPriority(i,j,priority,game)

    for row in range(0,3):
        for column in range(0,3):
            print(str(priority[row][column]) + " ", end = '')
        print()

    max = 0
    pos_x = 0
    pos_y = 0
    for i in range(0,3):
        for j in range(0,3):
            if priority[i][j] > max: 
                max = priority[i][j]
                pos_x = i
                pos_y = j

    game[pos_x][pos_y] = 2
    return game
  
def ticTacToeComputer():
    turn = 0
    game = [[0,0,0],
            [0,0,0],
            [0,0,0]]

    while not verifyWinnier(game):
        if turn % 2 == 0:
            game = playerTurn(1, game, turn)
        else : game = computerTurn(game, turn)
        turn += 1

def ticTacToeHuman():
    turn = 0
    game = [[0,0,0],
            [0,0,0],
            [0,0,0]]

    while not verifyWinnier(game):
        if turn % 2 == 0: game = playerTurn(1, game, turn)
        else : game = playerTurn(2, game, turn)
        turn += 1
        
def printPlayerMenu(player, game, turn):
    pos = [0,0]
    print("----------------Turn " + str(turn) + "-----------------")
    print("Player " + str(player))
    printGame(game)
    while True:
        pos[0] = int(input("row: ")) - 1
        pos[1] = int(input("column: ")) - 1
        if not ((pos[0] > 2 or pos[0] < 0) or (pos[1] > 2 or pos[1] < 0)): return pos
        else: print("Invalid position!")

def playerTurn(player, game, turn):
    while True:
        pos = printPlayerMenu(player, game, turn)
        if game[pos[0]][pos[1]] == 0: 
            game[pos[0]][pos[1]] = player
            return game
        else: print("Invalid position!")

def printMenu():
    print("--------------Tic Tac Toe--------------")
    print("1 - Play against human")
    print("2 - Play against computer")
    print("0 - Exit")
    option = input("Select: ")
    return option

while True:
    option = printMenu()
    if option == '1': ticTacToeHuman()
    elif option == '2':  ticTacToeComputer()
    elif option == '0': break
    else : print("Invalid option!")




