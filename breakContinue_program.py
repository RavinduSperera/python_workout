x =[12, 23, 567, 123, 88]

# using for loop 
# calculate the total value and the average
"""
total = 0

for i in x:
    total += i

print("Total: "+str(total))
print("Average: "+str(total/len(x)))

"""

# using for loop 
# find the min and max values 
"""
max = x[0]
min = x[0]

for i in x:
    if max < i:
        max = i # updating task
    if min > i:
        min = i # updating task

print("max is "+str(max))
print("min is: "+str(min))

"""

# usign while loop 
# calculate the total value and average
"""count = 0
total = 0

# need to recap this 
while count < len(x):
    item = x[count]
    total += item
    count += 1

print('Total: '+str(total))
print('Average: '+str(total/len(x)))"""

# using while loop 
# find the max and min values in given set 
count = 0
total = 0

min = max = x[0]

while count < len(x): # devare of this condition
    item = x[count] # need to asign item manually

    if item > max:
        max = item
    if item < min:
        min = item

    count += 1 # need to increase

print("Max is "+str(max))
print("Min is "+str(min))