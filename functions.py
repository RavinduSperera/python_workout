# functions

# with a user input
"""
marks = int(input("Enter your makrs here: "))

# creating a function
def get_grade():
    if marks >=35 and marks <= 100:
        print('Pass!')
    else:
        print('Fail!')

# calling the function
get_grade()

"""


# without user inputs -  with positional arguments
"""
def grade(subject, marks):
    print("Subject: "+subject)

    if marks >= 35 and marks <= 100:
        print('Pass!')
    else:
        print('Fail!')

# function calling 
grade('Math', 34)
grade('English', 75)

"""

# using default arguments
"""
def grade(mark, subject='unknown'):
    print('Subject: '+subject)

    if mark >= 35 and mark <= 100:
        print('Pass!')
    else:
        print('Fail!')

# function calling 
grade(78)

"""

# using named arguments - to identify properly
def grade(marks, subject):
    print('Subject: '+subject)

    if marks >= 35 and marks <= 100:
        print('Pass!')
    else: 
        print('Fail!')

# calling function 
grade(marks=75, subject='Maths')


