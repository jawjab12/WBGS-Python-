def dogYears(age):
    print("Calculating doggy age ...")
    age = age * 7
    return age
    


age = int(input("What is the age of your dog?"))
#dogYears(age)
age=dogYears(age)
print("Your dog is",age,"in dog years")

