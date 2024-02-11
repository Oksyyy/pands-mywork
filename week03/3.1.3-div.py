# 3.1.3-div.py
# Program that reads in two numbers and outputs the integer result and the remainder
# Author: Oksana Abrosimova

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
answer = x / y

print(f"{x} divided by {y} is {int(answer)} with remainder {x%y}")