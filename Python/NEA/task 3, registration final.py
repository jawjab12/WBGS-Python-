##########################
# AQA User Registration  #
##########################

 
"""
Amend your code from Exercise 1 so that it meets the following requirements:
Add comments so the code is self-documenting
When checking the username, the program should treat upper case letters and lower case letters as being the same. eg Userl is the same as userl
The user is allowed 3 tries to enter a username that has not already been used, before the program ends
. The user is allowed 3 tries to enter a password that is at least 12 characters long before the program ends.
 """
import getpass


userNames = ["user1", "user2", "user3", "user4", "user5"]

print("Welcome to AQA User Registration")



for i in range (3):
   
    userName = input("New username: ").lower()
   
    if userName in userNames:
        print("this username has been used before")
        userName=("")
       
    else:
        print("unique username!")
        break
else:
    print ("Locked out")
    exit()
   
for x in range (3):
    userPassword = getpass.getpass("Password (6-12 characters): ")

    if 6 <= len(userPassword) <= 12:
        print("password meets req")
        print(f"Your password is: \n  \n {userPassword} \n  \n Your username is \n \n {userName}")
        break
       
    else:
        print("Error: Password must be between 6 and 12 characters.")
else:
    print ("lcoked out")
    exit()
# end of program
