#  slicing - create a substring by extracting elements from another string
# indexing[]
# [start:stop:step]

name = 'bro code'

first_name = name[0]   # only printing a letter 
first_name = name[0:7] # displaying a word ([:7])
last_name = name[8:14] # displays last name ([8:])
funky_name = name[0:8:3] # this one make no sence
reversed_name = name[::-1] # reversing a string

print(reversed_name)