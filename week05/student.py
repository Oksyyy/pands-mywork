# student.py
# Program that puts stores student details and prints them out
# Author: Oksana Abrosimova

student = {
    'name' : 'Mary',
    'modules' : [
    {'course' : 'Programming',
     'grade' : 45},
    {'course' : 'History',
     'grade' : 99}
    ]
}

print(f"Student: {student['name']}")

for module in student['modules']:
    print(f"\t {module['course']} \t: {module['grade']}")