import random

cnumber=random.randrange (1,101)
userinput=int(input("Enter Your Number:-..."))

if userinput>cnumber:
    print("computer number",cnumber)
    print("Your guess number is high")
elif cnumber>userinput:
    print("Your guess number is to low")
else:
    print("computer number",cnumber)
    print("Your guess number is equal")
