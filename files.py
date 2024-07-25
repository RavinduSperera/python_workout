# files handling 

# open a file - open() - for reading and writing

file = open('file.txt', ) # need to add exact file location

# when file reading
"""
read() - reads complete file
readline() - reads line by line (use a loop)

content = file.readline()

"""
# when reading
"""
file modes:
    r - read only
    w - write with truncate
    x - open for exclusive creation
    a - append
    b - binary
    t - text mode
    + - updating

"""



print(content)

file.close() # closing a file is very important