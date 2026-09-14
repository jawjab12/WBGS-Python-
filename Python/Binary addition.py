def addition():
    if Bit1==1 and Bit2==0:
        return ("1 carry 0")
    elif Bit1==0 and Bit2==0:
        return ("0 carry ")
    elif Bit1==0 and Bit2==1:
        return ("1 carry 0 ")
    elif Bit1==1 and Bit2==1:
        return ("1 carry 0")
Bit1=int(input("First didgit"))
Bit2=int(input("2nd digit"))
if Bit1 and Bit2 == 1 or 0:
    print ("ok")
    print (addition())
    
    
else:
    print ("Only 1 or 0")
    
