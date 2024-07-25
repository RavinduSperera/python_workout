# highest marks for each subject - done
# height total mark holder of the data set

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
    # a dictionary
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

# function calling 
for subject, dataset in subject_marks.items():
    name, marks = get_top_student(subject, dataset)
    msg = f'Top student for {subject} is {name} with {marks}'
    print(msg)
