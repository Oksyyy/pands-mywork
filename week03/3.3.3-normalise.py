# normalise.py
# Program that reads in a string and removes leading/trailing spaces 
# It also converts the string to lower case
# It also outputs the length of the original string

original_string = input('Please enter a string:')
formatted_string = original_string.strip().lower()

print(f"That String normilised is: {formatted_string}")
print(f"We reduced the input string from {len(original_string)} to {len(formatted_string)}")