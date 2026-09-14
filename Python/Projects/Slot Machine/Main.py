"""***************************************************************************************
SLOT MACHINE COMPUTING PROJECT
*each spin cost 15 coins
****************************************************************************************"""
from random import randint
import time

#creating the highscore file if it dosent exist
f = open("Highscores.txt", "a")
f.close()

#defining varaibles
coins = int(100)
useless=1
slot =()
cashout=(bool(False))
highscore=()
bellcount=0
cherrycount=0
bananacount=0
dollarcount=0
skullcount=0
finish=bool(False)

#the spinner
def spinner():
    spin=randint(1,5)
    if spin == (1):
        return "Bell"
    elif spin == (2):
        return "Cherry"
    elif spin == (3):
        return "Banana"
    elif spin == (4):
        return "Dollar"
    elif spin == (5):
        return "Skull"

    
#print the first 6 lines of the leaderboard
def leaderboard():
    f = open("Highscores.txt", "r")
    print(f.readline())
    print(f.readline())
    print(f.readline())
    print(f.readline())
    print(f.readline())
    print(f.readline())
    f.close()

    
#writes your highscore
def write():
    f = open("Highscores.txt", "a")
    f.write(highscore)
    f.write("\n")
    f.close()
    
#clears the leaderboard if the user wants 
def clearchoice():
    clearc=input("Would you like to clear the leaderboard? (y/anyinput)")
    if clearc==("y"):
        f = open("Highscores.txt", "w")
        f.write("")
        f.close 
        print ("cleared!")
    else:
        print ("ok, Goodybye")


leaderboard()
print("*************************************")
name = input("Whats your name?: ")
#Asking the user if they want to continue or cash out 
while coins >0 and cashout ==False :
    ga=input("do you want to continue (y) or cashout? (c) or (y/c/):")
    if ga == ("y"):
        coins=(coins-15)
        bellcount=0
        cherrycount=0
        dollarcount=0
        bananacount=0
        skullcount=0
        
        result = [spinner(), spinner(), spinner()]
        print("**********************************")
        print (result[0])
        time.sleep(0.4)
        print (result[1])
        time.sleep(0.4)
        print (result[2])
        time.sleep(0.4)
        print("**********************************")
        
#BELL
        for item in result:
            if item == 'Bell': 
                bellcount=bellcount+1               
        if bellcount>0:

             useless=useless+1
        else:
            useless=useless+1
#CHERRY
        for item in result:
            if item == 'Cherry': 
                cherrycount=cherrycount+1              
        if cherrycount>0:

             useless=useless+1
        else:
            useless=useless+1
#BANANA
        for item in result:
            if item == 'Banana': 
                bananacount=bananacount+1              
        if bananacount>0:
 
             useless=useless+1
        else:
            useless=useless+1            
#DOLLAR
        for item in result:
            if item == 'Dollar': 
                dollarcount=dollarcount+1               
        if dollarcount>0:
             useless=useless+1
        else:
            useless=useless+1
#SKULL
        for item in result:
            if item == 'Skull':  
                skullcount=skullcount+1
               
        if skullcount>0:
            useless=useless+1
        else:
            useless=useless+1

        if skullcount==0:
    #3 of any fruit
            if cherrycount>0 and bananacount>0 and dollarcount<0 and bellcount<0:
                time.sleep(0.2)
                print ("3 of any fruit = 50 coins")
                coins = (coins+50)
                #print ("you have",coins,"coins")
        
    #2 of the same fruit
            elif cherrycount ==2 or bananacount==2:
                time.sleep(0.2)
                print ("2 of the same fruit = 30 coins")
                coins = (coins+50)
                #print ("you have",coins,"coins")
    #3 bells
            elif bellcount==3:
                time.sleep(0.5)
                print ("3 bells =1000")
                coins=(coins+1000)
                #print ("you have",coins,"coins")
    #3 cherry
            elif cherrycount==3:
                time.sleep(0.5)
                print ("3 cherrys =500")
                coins=(coins+500)
                print ("you have",coins,"coins")
    #3 banana
            elif bananacount==3:
                time.sleep(0.5)
                print ("3 bananas =700")
                coins=(coins+700)
               # print ("you have",coins,"coins")
    #2 bells
            elif bellcount==2:
                time.sleep(0.2)
                print ("2 bells=100")
                coins=(coins+100)
                #print ("you have",coins,"coins")
    #3 Dollars
            elif dollarcount==3:
                time.sleep(0.2)
                print ("all dollars =500")
                coins = (coins+500)
                #print ("you have",coins,"coins")
    #2 dollars
            elif dollarcount==2:
                time.sleep(0.2)
                print ("2 dollars=50")
                coins=(coins+50)
                #print ("you have",coins,"coins")
    #1 dollars
            elif dollarcount==1:
                time.sleep(0.2)
                print ("1 dollars=10")
                coins=(coins+10)
                #print ("you have",coins,"coins")

    #skull
            elif skullcount>1:
                print ("sorry you go skull")
            
        else:
            print ("sorry, you got skull")
            useless=useless-1
    elif ga ==("c"):
        print ("Cashing out...")
        cashout=True
        
    else:
        print ("invalid input, try again")
        ga=input("do you want to continue? (y/c)")
    print ("You have",coins,"coins")
if coins <=0:
    print (" you have no more coiuns please leave the gambling floor")
elif cashout ==True:
    print ("thank you for gambling with us")
    print ("you leave us today with",coins,"coins")
    highscore=str((name, ":" ,coins))
    write()
leaderboard()
clearchoice()
