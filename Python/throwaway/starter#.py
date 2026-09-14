#The below program asks a user to set a secret word.
#The word must be at least 6 characters long.
#If the word is 6 characters long it will be accepted
#If the word is less than 6 characters the user will be asked to enter a word again.
x = bool(True)
secret_word = ""
#write the correct condition for the while loop below#
while x == True  :
  secret_word = input ("Whats the word ")
  if len(secret_word) >= 6:
   print("Word accepted ")
   x=False
  else:
    print("choose a diff word ")
