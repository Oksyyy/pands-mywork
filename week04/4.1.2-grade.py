# grade.py
# Program that reads in students percentage mark and prints out corresponding grade
# Author: Oksana Abrosimova

grade = round(float(input("Enter the percentage: ")))
# assign percentage as a variable
# as part of extra tasks

if grade < 0 or grade > 100:
    print("Please enter a number between 0 and 100")
    # check if he percentage enterred is valid

if grade <40:
    print("Fail")
elif grade <50:
    print("Pass")
elif grade < 60:
    print("Merit2")
elif (grade) < 70:
    print("Merit1")
else:
    print("Distinction")