import time 
p=int(0)
dc = int(0)
print("Welcome to Jawaad’s and Akain’s pizza shop!")
print ("if you spend more than £15 you get 10% off")
print("Pizza list:")
print("(1)Pepperoni - £5")

print("(2)Margarita £3")

print("(3) Pineapple - £7")

i=0
x=0

pizza_order=input("how many pizzas do you want")

while i < pizza_order: 
    ans=int(input("What pizza do you want?"))
    if ans == int(1):
            print("you selected Pepperoni")
            p=(p+5)
            i=(i+1)
    elif ans == int(2):
            print ("you selected Margarita")
            p=(p+3)
            i=(i+1)
    elif ans == int(3):
            print ("you selected pinaple")
            p=(p+7)
            i= (i+1)

top = input ("would you like custom topping?")
if top == ("yes"):
    print ("extra cheese £2 (1) ")
    print ("gold flakes £10 (2) ")
    print ("caviar £20 (3) ")
    toppings=int(input("how many toppings do you want"))
    while x <toppings: 
        ans1=int(input("What topping do you want?"))
        if ans1 == int(1):
            print ("you selected extra  cheese")
            p = (p+2)
            x = (x+1)
        elif ans1 == int(2):
            print ("you selected gold flakes")
            p = (p+10)
            x = (x+1)
        elif ans1 == int(3):
            print ("you selected caviar")
            p = (p+20)
            x = (x+1)




if p > 15:
    p=(p*0.9)
    print ("you are saving 10%!")
    print ("your new total is £",+p)
else:
    print ("your total is £",+p)


dq = input ("would u like delivery?")
if dq == "yes":
    mile= (int(input("how far do you live?")))
    if mile <5:
            dc = (0)
            print ("free delivery")
            print ("please pay £",p)
    elif mile >10:
            print ("theres a 10 pound delivry charge")
            dc=(10)
            p=(p+dc)
            print ("your new total is",p)
    elif mile > 15:
            print ("sorry we dont deliver")
else:
    print ("okay, goodbye")





