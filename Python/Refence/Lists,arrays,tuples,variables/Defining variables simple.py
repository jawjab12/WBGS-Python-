"""****************************************
Asks the user for 5 names, then prints them'

*******************************************"""



def greeting (pos):
    list=["first","secound","thirds","fourth","fifth"]
    print("Hello "+list[pos]," person")
    name1 = input("Hello, what is your name?")
    print("Greetings",name1)
    nb_of_letters = len(name1)
    print("You have",nb_of_letters,"letters in your name.")
    return name1

name1=greeting(0)
name2=greeting(1)
name3=greeting(2)
name4=greeting(3)
name5=greeting(4)

print ("nice to meet you",name1,name2,name3,name4,name5)
