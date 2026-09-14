import random
"""**************************************************
Number guessing game 
*****************************************************"""
num = random.randint(1,10) 
guess = 0
guessesMade = 0
found = False
while guessesMade < 5 and found == False:
  guess = int(input('Can you guess my number bewteen 1 and 10?'))
  guessesMade= ( guessesMade +1)
  if guess < num:
    print("too low")
  elif guess > num:
      
    print ("too high") 
  else:
    print("You're right! My number was",num)
    print ("you used",guessesMade,"guesses")
    break
