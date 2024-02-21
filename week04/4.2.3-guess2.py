# guess2.py
# Program that keeps promting the user to guess a number until it's correct and indicatig whether the guess is too high or too low
# Author: Oksana Abrosimova

target_number = 30

guess = int(input('Please guess the number: '))

while guess != target_number:
    if guess > target_number:
        print("Too high")
    elif guess < target_number:
        print("Too low")
    
    guess = int(input('Please guess again: '))
 
else:
    print(f"Well done! Yes the number was {target_number}")