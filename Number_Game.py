import random
Target=random.randint(1,50)

while True:
    UserChoice=input("Guess a number or to Quiet the game type 'Q'")
    if(UserChoice=="Q"):
        break
    UserChoice=int(UserChoice)
    if(UserChoice==Target):
        print("Congratulations")
        print("You choose the Right number")
        break
    elif(UserChoice>Target):
        print("Please choose a Small number")
    else:
        print("Please choose a big number")
print("!____Game(..) Over____!")        