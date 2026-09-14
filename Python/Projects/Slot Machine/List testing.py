import time
from random import randint
coins =100
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

result = [spinner(), spinner(), spinner()]
print (result[0])
time.sleep(1)
print (result[1])
time.sleep(1)
print (result[2])
time.sleep(1)

bellcount=0
cherrycount=0
bananacount=0
dollarcount=0
skullcount=0

for item in result:
    if item == 'Bell': # change this to Bell and see what happens 
        bellcount=bellcount+1
       
if bellcount>0:
    print("bell found!",bellcount,"times")
else:
    print("bell not found!")


for item in result:
    if item == 'Cherry': # change this to Bell and see what happens 
        cherrycount=cherrycount+1
       
if cherrycount>0:
    print("chery found!",cherrycount,"times")
else:
    print("cherry not found!")


for item in result:
    if item == 'Banana': # change this to Bell and see what happens 
        bananacount=bananacount+1
       
if bananacount>0:
    print("chery found!",bananacount,"times")
else:
    print("Banana not found!")

for item in result:
    if item == 'Dollar': # change this to Bell and see what happens 
        dollarcount=dollarcount+1
       
if dollarcount>0:
    print("Dollar found!",dollarcount,"times")
else:
    print("dollar not found!")


for item in result:
    if item == 'Skull': # change this to Bell and see what happens 
        skullcount=skullcount+1
       
if dollarcount>0:
    print("skull found!",skullcount,"times")
else:
    print("skull not found!")


if skullcount<0:
    #3 of any fruit
    if cherrycount>0 and bananacount>0 and dollarcount<0 and bellcount<0:
        print ("3 of any fruit = 50 coins")
        coins = (coins+50)
        
    #2 of the same fruit
    elif cherycount ==2 or bananacount==2:
        print ("2 of the same fruit = 10 coins")
        coins = (coins+10)
    #3 bells
    elif bellcount==3:
        print ("3 bells =1000")
        coins=(coins+1000)
    #2 bells
    elif bellcount==2:
        print ("2 bells=100")
        coins=(coins+100)
    #3 Dollars
    elif dollarcount==3:
        print ("all dollars =500")
        coins = (coins+500)
    #2 dollars
    elif dollarcount==2:
        print ("2 dollars=50")
        coins=(coins+50)
    #1 dollars
    elif dollarcount==1:
        print ("1 dollars=10")
        coins=(coins+10)
else:
    print ("sorry you go skull")


