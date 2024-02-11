# 3.1.5-randomfruit.py
# Program that prints out random fruit
# Author: Oksana Abrosimova

import random
fruits = ['Apple', 'Orange', 'Banana', 'Pear']

index = random.randint(0, len(fruits)-1)
fruit = fruits[index]
print(f"A random fruit: {fruit}")