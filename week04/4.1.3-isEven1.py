# isEven1.py
# Program that reads in a number and evaluates of that number is Even or Odd
# The program keeps prompting the user to enter a number until the user enters -1
# Author: Oksana Abrosimova

number = int(input('Enter an integer: '))

while number >= 0:
        number -= 1
        if (number % 2) == 0:
            print(f"{number} is an even number")
        else:
            print(f"{number} is an odd number")
    
    