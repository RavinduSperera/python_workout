# files handling 

# open a file - open() - for reading and writing

file = open('file.txt', 'a') # need to add exact file location

# when file reading
"""
read() - reads complete file
readline() - reads line by line (use a loop)

content = file.readline()

"""
# when reading
"""
file modes:
    r - read only (default)
    w - write with truncate
    x - open for exclusive creation
    a - append
    b - binary
    t - text mode
    + - updating

"""

x = [str(i * 2) for i in range(0, 100)]

msg = '\n'.join(x)

file.write(msg)

file.close() # closing a file is very important


"""
# fixing the , adding issue at the end using join()
x = ['1', '2', '3', '4']
print(type(x))
msg = ','.join(x) # all the list elements need to be strings
print(msg)"""