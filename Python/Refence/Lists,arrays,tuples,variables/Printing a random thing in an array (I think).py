from random import randint

coms=["sdsdwsd","dsfdfdf","sfddffd","wdwddwdw"]

def gennum():
    olist=[1,2,3]
    
    num=randint(1,6)
    print(num)
    if num in olist:
        print(coms[num-1])


        


for i in range(6):
    gennum()
