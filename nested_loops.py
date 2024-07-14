# creating a rectange using nested for loops

rows = int(input('How many rows: '))
columns = int(input('How many columns: '))
symbol = input('Enter a symbol to use: ')

for i in range(rows):
    for j in range(columns):
        print(symbol, end='') # inner for loop
    print() # outter for loop 