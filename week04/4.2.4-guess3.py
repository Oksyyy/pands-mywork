# guess3.py
# Program that generates a random number from 0 to 100 to guess a target number until it's correct and indicatig whether the guess is too high or too low
# Author: Oksana Abrosimova


target_number = 30
# assign number to guess

import random
#import randon module to execute random number generation

guess = random.randint(0, 100)
# set the range for random number generation

while guess != target_number: # while loop condition for when generated random number doesn't match assigned number to guess
    if guess > target_number:
        print(f"{guess} is too high. Please guess again")
        # if generated number is above the number to guess - prompt a message that the number is too high
    elif guess < target_number:
        print(f"{guess} is too low. Please guess again")
        # if generated number is below the number to guess - prompt a message that the number is too low
    
    guess = random.randint(0, 100)
    # instruct the loop to continue
 
else:
    print(f"Well done! Yes the number was {target_number}")
    # when the number is guessed correctly print a statement that the guess was correct and finish the loop