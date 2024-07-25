# Task 1 - highest marks for each subject - done
# Task 2 - height total mark holder of the data set - done but not correct

# mapper function **
def get_marks(record: tuple):
    return record[1]

# function to find the max marks holder student for each subject 
def get_top_student(subject: str, dataset: dict):
    max_marks = 0
    max_student = ''

    for name, marks in dataset.items():
        if max_marks < marks:
            max_marks = marks
            max_student = name
    
    return max_student, max_marks

lines = None
with open('data.txt') as file:
    lines = file.readlines()

# error handling
if not lines: 
    print('Something went wrong!')
    exit()

marks_lines = lines[1:] # from line 1 to end line

subject_marks = {
    # a dictionary for task 1
}
student_marks = {
    # a dictionary for task 2 
}

for line in marks_lines:
    entries = line.split(',') # separate from a , - split()

    name = entries[0].strip() # cuttin/ remove spaces - strip()
    subject = entries[1].strip()
    marks = int(entries[2].strip())

    if subject not in subject_marks:
        subject_marks[subject] = {
            # a disctionary
        }
    
    subject_marks[subject][name] = marks

    prev_marks = student_marks.get(name, 0)
    student_marks[name] = prev_marks + marks

messages = [] # creating a list for write file

# function calling 
for subject, dataset in subject_marks.items():
    name, marks = get_top_student(subject, dataset)
    msg = f'Top student for {subject} is {name} with {marks}'
    print(msg)
    messages.append(msg)

# print(student_marks)

marks_list = [ (name, marks) for name, marks in student_marks.items()]

marks_list.sort(key=get_marks, reverse=True)
top = marks_list[0]
msg = f'Top student is {top[0]} with {top[1]} marks.'
messages.append(msg)
print('') # this is for a space between tasks
print(msg)

with open('results.txt', 'w') as output_file:
    for msg in messages:
        output_file.write(msg)
        output_file.write('\n')






# issue
"""
Something is wrong with this program. The calculations were not properly implemented. 
recheck **

the answer should be 
    Top student for Science is Kusum with 90
    Top student for Sinhala is Kelum with 96
    Top student for Math is Praneeth with 85

    Top student is Kusum with 211 marks.

"""