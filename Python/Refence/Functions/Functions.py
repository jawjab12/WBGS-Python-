def id ():
    number=int(input("enter number"))
    return number

def processData(number):
    squaredNumber = number * number
    return squaredNumber

def outputAnswer(squaredNumber):
    print("The square of your number is",squaredNumber)
    
def main():
    usersNumber = inputData()
    userSquaredNumber = processData (usersNumber)
    outputAnswer (userSquaredNumber)
    

