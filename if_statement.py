# if statement

age = int(input('Enter your age: ')) # typecasting bcs an int input

if age >= 18:
    print('You are an Adult.')
elif age < 18:
    print('You are a child.') # else if - elif
else:
    print('Error!')


# using a sigle line - ternary operator
age = 'adult' if age>=18 else 'child'