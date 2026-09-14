from random import randint
import random
import time



def appeal():
    
    bowl=randint(1,7)
    if bowl == 1:
        print ("review pending...")
        time.sleep (1.5)
        print ("bowled")
        time.sleep (1.5)
        return (1)
    elif bowl == 2:
        print ("review pending...")
        time.sleep (1.5)
        print ("caught")
        return (1)
    elif bowl == 3:
        print ("review pending...")
        time.sleep (1.5)
        print ("Run out")
        return (1)
    elif bowl == 4:
        print ("review pending...")
        time.sleep (1.5)
        print ("L-B-W")
        return (1)
    elif bowl ==7:
        time.sleep(1.8)
        print ("Going to 4th umpire")
        time.sleep(1.8)
        print ("Checking ultraedge")
        time.sleep(1.8)
        print("revieving secound opinion")
        time.sleep(1.8)
        review=random.randint(1,2)
        if review==1:
            time.sleep(1.8)
            print ("not out")
            return (0)
        else:
            time.sleep(1.8)
            print ("out")
            return (1)
    else:
        print ("review pending...")
        time.sleep (1.5)
        print ("not out")   



score=0
batters = int(10)
balls = 30

while batters>0 and balls >0:
    
#for n in range (10):
    for i in range (6):
        bowl=randint(1,6)
        time.sleep (1)
        print ("you hit a",bowl)
        if bowl == 1:
            score = (score+1)
            balls=balls-1
        elif bowl == 2:
            score = (score+2)
            balls=balls-1
        elif bowl == 4:
            score = (score+4)
            balls=balls-1
        elif bowl == 6:
            score = (score+6)
            balls=balls-1
    
        else:
            appeal()
            result = appeal()
            
            batters = (batters - appeal())
            print ("batters left:",batters)
            balls =balls-1
used = 30-balls
print ("total",score)
print ("balls left",balls,"batters left",batters)
print ("balls used",used)
