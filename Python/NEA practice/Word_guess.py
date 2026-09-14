"""*******************************************
WORD GUESSR
******************************************"""
import time
tries = bool(True)
count = int(0)

def spam_space():
    for i in range (50):
        print ("\n")

def check (guess):
    print ("Check") 



    
U1= input ("Player 1 name: ")
U2= input ("Player 2 name: ")


secret = input (U1+" ,please enter your secret word")
time.sleep (0.5)
print ("hiding secret word")
time.sleep (0.5)
print ("...")
spam_space()
print ("continue from here:")
while count > 3:
    tries = False 

while tries == True:
    guess = input (U2+" ,guess one letter for the word: ")
    count= (count +1)
    print (check)
    
while tries == False:
    wordguess = input (U2+" ,guess  the word: ")
    if wordguess == secret:
        print (U2+"Wins")
    else:
        print (U1+"Wins")
