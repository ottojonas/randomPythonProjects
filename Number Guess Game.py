#Works, want to make the game continue if the user does not use a number in range 1-10

import random

num = random.randint(1, 10) 
guess = None 

while guess != num: 
    guess = input("Guess a number between 1 and 10: ")
    guess = int(guess)

    if guess == num: 
        print("You got it!")
        break 

    else:
        print("Nope, sorry. Try again!")