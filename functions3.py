# return - sending values to the person who calling the function

"""
def get_grade(marks):

    if marks >= 35 and marks <= 100:
        return 'pass!'
    else:
        return 'falied!'

# function calling and store the passed value
grade = get_grade(-5)

# print the stored value
print(grade)

"""

# proper way 
def get_grade(subject, marks):
    
    if marks >= 35 and marks <= 100:
        grade = 'pass!'
    else:
        grade = 'failed!'

    return subject, grade

grade = get_grade('Science', 67)
print(grade)