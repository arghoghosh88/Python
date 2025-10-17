import random
Target=random.randint(1,50)
# First Two line for guessing number from compiler.
while True:
    # This below line for input a number from user
    UserChoice=input("Guess a number or to Quiet the game type 'Q'") 
    if(UserChoice=="Q"):
        break
        # There are three casses user can quit the game by press "Q" or he/she can continue by input numbers.
        # Number will be smaller or greater than the the number guessed by the compiler.
        # If user guess the right number then the game will end else it will continue until he/she will get the right number or press "Q"
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
