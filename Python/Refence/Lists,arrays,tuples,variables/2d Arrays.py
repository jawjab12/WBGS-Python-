"""**********************************************************
Makes a 2d list and prints a specifc item
***********************************************************"""


"""My2dArray=[[1,2,3], [6,7,8], [34,44,56]] 

My2dArray.insert(3, [100,120,123])
print (My2dArray)
"""


"""1. Create a 2D array called ClassMates containing:
• The first row [0] index will contain 3 classmates’ names from your ComSci class
• The second row [1] will contain 3 classmates’ names from your Maths class
• The third row [2] will contain 3 classmates’ names from your Form group
2. Print out the 2nd person in your computer Science class
3. Print out the 1st person in your Maths class
4. Print out the number of rows in your 2D array
5. Insert a 4th row in this add 3 class mates in your Science class 
6. Print out the whole 2d Array
Create both the python and pseudocode solutions and include the evidence below:
2"""

classmates = [["neev","akain","shuuuujagesh"],[ "haruto","om.p","yusuf"],["ethan","mikhial","tyler"]]
print (classmates [0][1])
print (classmates [1][0])
print (len(classmates))
classmates.insert (3,"william","tyler","ishaan")
print (classmates)
