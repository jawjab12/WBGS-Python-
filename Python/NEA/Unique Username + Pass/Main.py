##########################
# AQA User Registration  #
##########################
 
import getpass



userNames = ["User1", "User2", "User3", "User4", "User5"]

print("Welcome to AQA User Registration")

userName = input("New username: ")

if userName in userNames:
    print("this username has been used before")
    exit()
else:
    print("unique username!")


userPassword = getpass.getpass("Password (6-12 characters): ")

if 6 <= len(userPassword) <= 12:
    print("password meets req")
    print(f"Your password is: \n  \n {userPassword} \n  \n Your username is \n \n {userName}")  
else:
    print("Error: Password must be between 6 and 12 characters.")

# end of program
