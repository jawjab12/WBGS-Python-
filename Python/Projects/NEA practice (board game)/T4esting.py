#the board game has to be two player
#the objective of the game is to get to the end of the 20 space board
#Each player must alternate turns and roll a 6 sided die to see how many spaces to move
#when a player reaches the last space, they win and the game ends
#the die must only be rolled when the player whose turn it is presses a key
#Each turn, each player’s board should be printed and there should be a message that tells the players whose turn it is
#when the game ends, a message should be printed declaring the winner

import time
from random import randint

#Creating 1D arrays for the board
Board1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Board2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#Creating a win condition
move1 = 0
move2 = 0
win1 = bool(False)
win2 = bool(False)
player1=bool(False)
player2=bool(False)
turncount=bool(False)
finish = bool(False)




#Creating a dice roll
def Die1():
    die1= randint(1,6)
    winCount1 = int(0)
    winCount1 = winCount1 + die1 
    return die1
    #for development purposes
    return winCount1

def Die2():
    die2= randint(1,6)
    winCount2 = int(0)
    winCount2 = winCount2 + die2 
    return die2
    #for development purposes
    return winCount2

while finish ==False:
    time.sleep(0.4)
    print("***************************************************")
    time.sleep(0.4)
    print("PLAYER 1 TURN:")
    turn1 = input("PRESS SPACE TO ROLL")
    if turn1 == (""):
        number1 = Die1()
        time.sleep(0.7)
        print("PLAYER 1 ROLLED ", number1)
        move1 = (move1+number1)
        turncount = bool(True)
        if move1 + number1 >= 19:
            winCount1 = 19
            move1 =19 
        Board1[move1]=1
        print(Board1)
        print (finish)
        time.sleep(0.4)
        print("***************************************************")
        time.sleep(0.4)
        

    else:
        time.sleep(0.4)
        print("INVALID INPUT")
        time.sleep(0.4)
        print("***************************************************")
        time.sleep(0.4)

    time.sleep(0.4)
    print("PLAYER 2 TURN:")
    turn2 = input("PRESS 'SPACE' TO ROLL")


    if turn2 == (""):
        number2 = Die2()
        time.sleep(0.7)
        print("PLAYER 2 ROLLED ", number2)
        move2 = (move2+number2)
        turncount = bool(False)
        if move2 + number2 >= 19:       
            finish = bool(True)
            winCount2 = 19
            move2 =19
        
        Board2[move2]=1
        print(Board2)
        print (finish)

      
    else:
        time.sleep(0.4)
        print("INVALID INPUT")
        time.sleep(0.4)
        print("***************************************************")
        time.sleep(0.4)

    if move1 == 19:
        finish = True
    elif move2 == 19:
        finish = True
        


  


















