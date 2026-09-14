"""********************************************************************
SIMPLE BOARD GAME 
**********************************************************************"""
#importing variables 
from random import randint

#the board must have 20
board1 =[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
board2 =[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#Defining variables
win = bool(False)
win2 = bool(False)
play1=bool(False)
play2=bool(False)
turncount=bool(False)
turncount2=bool(False)
move = 0
move2=0
end = False   

#Checking if someone has won 
if board1[19]=="1":
    win = True
    play1=bool(True)
elif board2[19]=="1":
    win = True
    play2=bool(True)
    
# roll a 6 sided dice 
def roll():
    roll=randint(1,6)
    moveCount=int(0)
    moveCount=moveCount+roll
    return roll
#for debuggin reasons 
    return moveCount


# roll a 6 sided dice 
def roll2():
    roll2=randint(1,6)
    moveCount2=int(0)
    moveCount2=moveCount2+roll2
    return roll2
#for debuggin reasons 
    return moveCount
#Getting names
user1=input ("what is persons 1's name")
user2=input ("what is persons 2's name")


#PLAYER 1 TURN
while turncount == False:
    while win==False:
        print("Player 1 Turn")
        rollCheck=input("Press enter to roll")
        if rollCheck == (""):
            value=roll()
            print ("you rolled ",value,)
            move=(move+value)
            
            if move + value >=19:
                win=True
                moveCount=19
                move=19

            board1[move]=1
            print (board1)
            print (win)
            turncount=True
        else:
            print ("invalid")
            break

"""#Player 2 turn      
while turncount == True:
    while win2==False:
        print("Player 2 Turn")
        rollCheck2=input("Press enter to roll")
        if rollCheck2 == (""):
            value2=roll2()
            print ("you rolled ",value2,)
            move2=(move2+value2)
            if move2 + value2 >=19:
                win=False
                moveCount2=19
                move2=19

            board2[move]=1
            print (board2)
            print (win)
            turncount=False
        else:
            print ("invalid input")
            break

"""


#the winner must be declared at the end
