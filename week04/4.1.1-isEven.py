# isEven.py
# Program that reads in a number and evaluates of that number is Even or Odd
# Author: Oksana Abrosimova

number = int(input("Enter an integer: "))
if (number % 2) == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")