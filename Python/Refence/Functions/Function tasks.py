# Adding
def numberAdder(num):
    num = (num+1)
    return num

a=numberAdder(4)
print (a)

#A function that ask a user politely for their name,
#says “hello <name>”, then returns their name to the main program.

def prog (name):
    print ("hello",name)
inputedName= input ("whats your name")
prog (inputedName)



# A function that counts the number of times the letter
#a is in their name, and returns that number.

def aSearch():
    name = input("what is your name?")
    total = 0
    for i in range (len(name)):
     if name[i] == "a":
         total= total +1
    print("The letter a is used",total)

aSearch()

vowels= ["a","e","i","o","u"]
def vSearch():
    name = input("what is your name?")
    total = 0
    for i in range (len(name)):
     if name[i] == vowels:
         total= total +1
    print("Vowles are used ",total)
if "a" in vowels:
    print ("sure")
vSearch()
