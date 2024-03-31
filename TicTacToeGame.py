from cmath import inf


def EvaluationFunction(gb):
    for y in range(0,3):
        if gb[0][y]==gb[1][y]==gb[2][y]=='X':
            return 'X'
        if gb[0][y]==gb[1][y]==gb[2][y]=='O':
            return 'O'
    
    for x in range(0,3):
            if gb[x][0]==gb[x][1]==gb[x][2]=='X':
                return 'X'
            if gb[x][0]==gb[x][1]==gb[x][2]=='O':
                return 'O'
    
    if gb[0][0]==gb[1][1]==gb[2][2]=='X' or gb[0][2]==gb[1][1]==gb[2][0]=='X':
        return 'X'
    if gb[0][0]==gb[1][1]==gb[2][2]=='O'or gb[0][2]==gb[1][1]==gb[2][0]=='O':
        return 'O'
    
    for x in range(0,3):
        for y in range(0,3):
            if gb[x][y]=='':
                return True  #continue game
                
    return  False   #game draw


def MakeMove(gb,player):
    if player=='X':
        besteval=float('-inf')
        bestmove=None
        for x in range(0,3):
            for y in range(0,3):
                if gb[x][y]=='':
                    gb[x][y]=player
                    eval=Minimax(gb,True)
                    gb[x][y]=''
                    if eval>besteval:
                        besteval=eval
                        bestmove=(x,y)
        if bestmove is not None:                
            gb[bestmove[0]][bestmove[1]]=player
        return True
        
    if player=='O':
        besteval=float('-inf')
        bestmove=None
        for x in range(0,3):
            for y in range(0,3):
                if gb[x][y]=='':
                    gb[x][y]=player
                    eval=Minimax(gb,True)
                    gb[x][y]=''
                    if eval>besteval:
                        besteval=eval
                        bestmove=(x,y)
        if bestmove is not None:                
            gb[bestmove[0]][bestmove[1]]=player
        return True






def Minimax(board,is_max):
    if EvaluationFunction(board)=='X':
        return 1
    if EvaluationFunction(board)=='O':
        return -1
    if not EvaluationFunction(board):#draw
        return 0
        
    if is_max:
        max_eval=float('-inf')
        for x in range(0,3):
            for y in range(0,3):
                if board[x][y]=='':
                    board[x][y]='O'
                    eval=Minimax(board,False)
                    board[x][y]=''
                    max_eval=max(max_eval,eval)
        return max_eval
    else:#minimizing
        min_eval=float('inf')
        for x in range(0,3):
            for y in range(0,3):
                if board[x][y]=='':
                    board[x][y]='X'
                    eval=Minimax(board,True)
                    board[x][y]=''
                    min_eval=max(min_eval,eval)
        return min_eval            
                    
                        

def DisplayGameBoard(board):
    for row in board:
        
        print(" | ".join(row))
        print("---------")


import random        
import time
import random
import time

def StartGame(gb, firstturn,opt):
    Game = True
    turn = 0
    player = ['X', 'O']
    
    while Game:
        # DisplayGameBoard(gb)
        
        if firstturn:
            # Generate random indices for the first player
            x1 = random.randint(0, 2)
            y1 = random.randint(0, 2)
            gb[x1][y1] = player[0]
            DisplayGameBoard(gb)
            print("Opponent Thinking ....")
            time.sleep(2)
            firstturn = False
            if opt==1:
                x=int(input("enter row 0-2"))
                y=int(input('enter column 0-2'))
                gb[x][y]=player[1]
                DisplayGameBoard(gb)
                turn=1
                # break
            else:
                while True:
                    x2 = random.randint(0, 2)
                    y2 = random.randint(0, 2)
                    if x2 != x1 and y2 != y1:
                        gb[x2][y2] = player[1]
                        DisplayGameBoard(gb)
                        print("Opponent Thinking ....")
                        time.sleep(2)
                        turn = 1
                        break
            
        if turn == 1:                    
            MakeMove(gb, player[0])
            turn = 2
            DisplayGameBoard(gb)
            print("Opponent Thinking ....")
            time.sleep(2)
        
        if turn == 2:
            if opt==1:
                x=int(input("enter row 0-2"))
                y=int(input('enter column 0-2'))
                gb[x][y]=player[1]
                turn=1
                DisplayGameBoard(gb)
 
            else:    
                MakeMove(gb, player[1])
                turn = 1
                DisplayGameBoard(gb)
                print("Opponent Thinking ....")
                time.sleep(2)

        if not EvaluationFunction(gb):
            Game = False
            print("Game draw")
            DisplayGameBoard(gb)
        if EvaluationFunction(gb) == 'X':
            print('X wins') 
            DisplayGameBoard(gb)
            Game = False  # Game ends
        if EvaluationFunction(gb) == 'O':
            print('O wins')
            DisplayGameBoard(gb)
            Game = False  # Game ends



opt=int(input("Human Vs Ai (1) or Ai Vs Ai (2)"))
    
            
gb=[
    ['','',''],
    ['','',''],
    ['','','']
]            
StartGame(gb,True,opt)            