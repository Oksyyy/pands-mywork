# average.py
# Program that reads numbers until the user enters a 0 and appends them into a list. 
# It then prints out each of the numbers and the average of them

numbers = []
#set list of numbers for loop

number = int(input("Enter a number (0 to quit): "))
# prompt the user to enter a number

while number != 0: 
    numbers.append(number)
    # while condition to quit is not met append the number user enterred into the numbers list for the loop to evaluate

    number = int(input("Enter another (0 to quit): "))
    # prompt the user to enter the number again if the enterred number doesn't meet the condition to quit

for i in numbers:
    print(i)
    # once the loop was quit print out all enterred numbers

average = sum(numbers)/ len(numbers)
# calculate the average value of all enterred numbers

print(f"The average is {average}")

