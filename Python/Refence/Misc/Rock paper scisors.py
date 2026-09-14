import random




"""**************************************************
Rock paper scissors game 
*****************************************************"""
                                    
userint=int(0) 
Choice = random.randint(1,3)

userchoice=input("whats your choice, rock paper or scisors: ")

if userchoice == ("rock"):
    userint=(userint+1)
    
elif userchoice == ("paper"):
    userint=(userint+2)
    
elif userchoice == ("scissor"):
    userint=(userint+3)
else:
    print ("invalid choice")
#Rock+rock
if userint==(1) and Choice==(1):
    
    print ("draw")
#rock+ paper
if userint==(1) and Choice==(2):
    print ("you lost , paper beats rock")
    
#rock+scissors
if userint==(1) and Choice==(3):
    print ("you won, rock beats scissors")


#paper+rock
if userint==(2) and Choice==(1):
    print ("you won, rock beats paper")
    
#paper+paper
if userint==(2) and Choice==(2):
    print ("Draw")
    
#paper+scissors
if userint==(2) and Choice==(3):
    print ("you lost, scissors beats paper ")


#scissors+rock
if userint==(3) and Choice==(1):
    print ("You lost, rock beats scisors ")
if userint==(3) and Choice==(2):
    print ("You lost, rock beats scisors ")

#scissors+scissors 

#scissors+paper 
if userint==(3) and Choice==(2):
    print ("You lost, rock beats scisors ")

#scissors+scissors 
if userint==(3) and Choice==(3):
    print ("Draw")



