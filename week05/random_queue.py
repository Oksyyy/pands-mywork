# random_queue.py
# Program that puts 10 random numbers into a queue and outputs all values in the queue 
# It then takes numbers from the queue one by one and prints out the remaining number still in the queue
# Author: Oksana Abrosimova

import random # import module for random number generation

queue = [] # create an empty list for numbers queue

number_count = 10 # assigning the number of numbers to be generated in the list

for x in range(number_count): # setting a range to run the loop the number of times specified by number_count variable
    queue.append(random.randint(0,100)) # appends adds a number to the end of the list. Random.randint generates a random number in a given range i.e. 0-100

print(f"queue is {queue}")

while len(queue) != 0:
    current_number = queue.pop(0)
    print(f"current number is {current_number} and the queue is {queue}")

print(f"the queue is now empty")
 
