"""Write a program that creates and initialises a 2D array to hold these five sets of marks:
Set 1: 80, 59, 34, 89
Set 2: 31, 11, 47, 64
Set 3: 29, 56, 13, 91
Set 4: 55, 61, 48, 0
Set 5: 75, 78, 81, 91
Extend your program so that it calculates and displays the highest mark, the lowest mark and the average mark achieved.
"""


"""Scores=[[80,59,34,89],[31,11,47,64],[56,13,91],[55,61,48,0],[75,78,81,91]]
print (Scores)


def countem(rownum):
    total=0
    for i in range (len(Scores[rownum])):
        total=total+Scores[rownum][i]
    return(total)

   
for i in range (len(Scores)):
    rowtotal=countem(i)
     
    print(rowtotal)
"""

make=input("make?")
model=input("model?")
colour=input("colour?")
print ("NEXT CAR")
make2=input("make?")
model2=input("model?")
colour2=input("colour?")
print ("NEXT CAR")
make3=input("make?")
model3=input("model?")
colour3=input("colour?")
print ("NEXT CAR")
make4=input("make?")
model4=input("model?")
colour4=input("colour?")
print ("NEXT CAR")
make5=input("make?")
model5=input("model?")
colour5=input("colour?")
carList = [[(make),(model),(colour)],[(make2),(model2),(colour2)],[(make3),(model3),(colour3)],[(make4),(model4),(colour4)],[(make5),(model5),(colour5)]]


print (carList)
