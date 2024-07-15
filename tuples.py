# tuple - collection which is ordered and unchangeable
#         used to group together related data
#         very similar to list but its uneditable and ordered

student = ('Bro', 21, 'male')

print(student.count('Bro')) # count the value
print(student.index('male')) # give the position
print('')

for z in student: # prints all the values inside th tuple
    print(z)
print('')

if 'bro' in student: # tuple with if statement
    print('Bro is here!')
else: 
    print("It is missing!")