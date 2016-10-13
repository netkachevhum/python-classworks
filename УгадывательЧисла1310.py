import random

def npt():
    #return int(input("Enter a number"))
    return random.randrange(1,10)

c = False 

a=random.randrange(1,10)
b=npt()


if a==b:
    print("Computer:",b)
    print(b, "is correct")
    c = True


while a != b:
    if b<a:
        print("Computer:",b)
        print("Incorrent, the value is bigger than ",b)
        b = npt()
    elif b>a:
        print("Computer:",b)
        print("Incorrect, the value is smaller than ",b)
        b = npt()
if not c:    
    print("Computer:",b)
    print(b,"is correct")







