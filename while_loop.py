# while

# method 1
name = None

while not name == 0:
    name = input('Enter your name: ')

print('Hello, '+name)


# method 2
name = ''

while len(name) == 0:
    name = input('Enter your name: ')

print('Hi '+name)