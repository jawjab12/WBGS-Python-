Username = ("Student1")
Password = ("WatfordLetMeIn")
#Allows the user one attempt to log in i.e. enter correct username and password
#If both the username and password are correct welcome the user to the network
#If either the username or password is incorrect output "access denied"
#Extension: Limit the user to 3 attempts
tries = 0 

while tries < 3:
    user =input("whats the username?")
    passw = input("whats the password")
    if user == Username and passw == Password:
        print ("allowed")
        break
    else: 
        tries = tries + 1 
        
