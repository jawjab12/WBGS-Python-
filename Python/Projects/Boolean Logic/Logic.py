a=userinput("Whats A")
b=userinput("Whats B")
choice=userinput("What gate do you want ")
def not_gate(a,):
    if a == 1:
        return 0
    elif a == 0:
        return 1
    else:
        return ("error")
if choice == "not":
    print (not_gate())
