# student1.py
# Program that reads in student details, stores then and and prints them out
# Author: Oksana Abrosimova

student = {} # create an empty dictionary

name = input("Enter your name: ") # prompt the student to enter their name 

student['name'] = name # assign variable name as the first dictionary key

modules = [] # create an empty list as a placeholder for course names and grades

course_name = input("Enter course_name: ") # prompt the student to enter course name
while course_name != '': # set a condition while the course name is not blank to perform the below actions
    course = {} # set an empty dictionary for the first course name
    course['course_name'] = course_name 
    # assign the variable course_name as the first key in the 'course' dictionary along with the enterred value (first pair)
    
    course['grade'] = input(f"Enter your grade for {course_name} ") 
    # assign the variable grade as the second key ib the course dictionary along with the entered value
    # this concludes course 1

    modules.append(course) # add course 1 to the module empty list 

    course = {} # set a second empty dictionary for the second course
    course_name = input("Enter course_name: ") # prompt the user to enter course name 
    # at this point the program goes back the the earlier condition > while course_name != ' ' and execute the loop again
    student['modules'] = modules

print("Student name: {name} ")
for course in   student['modules']:
    print(f"\t {course['course_name']}: \t {course['grade']}")