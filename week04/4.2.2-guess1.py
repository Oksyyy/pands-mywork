# guess1.py
# Program that keeps promting the user to guess a number until it's correct
# Author: Oksana Abrosimova

target_number = 30

guess = int(input('Please guess the number: '))

while guess != target_number:
    print("Wrong")
    
    guess = int(input('Please guess again: '))
 
else:
    print(f"Well done! Yes the number was {target_number}")

        