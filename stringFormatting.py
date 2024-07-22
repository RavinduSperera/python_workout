# strings formatting

height = 176
name = 'Ravindu Perera'

# method 1 - C type formatting
"""message = 'Hello %s, Your heigjt is %d.' %(name, height)"""

# method 2 - .format() - can do indexing as well 
# name = 0 and height = 1 (indexes)
"""message = 'Hello {}, your height is {}'.format(name, height)"""

# method 3 - f string formatting - recomended
"""message = f'Hello {name}, Your height is {height}'"""

# method 4 - general way
message = 'Hello '+name+' Your height is '+str(height)

print(message)