# conditional statements - grade generator according to the marks

marks = int(input('Enter your makr here: '))

if marks >= 75:
    print('Congratulations!, You have an A Grade.')
    print('Subject Marks: '+str(marks))

elif marks >=60 and marks <=75:
    print('Congradulations!, You have a B Grade.')
    print('Subject Marks: '+str(marks))

elif marks >= 50 and marks <=60:
    print('Congradulations!, you got a C Grade.')
    print('Subject Marks: '+str(marks))

else:
    print('We are so regret to say that you have failed')
    print('Try again!')


# using a single line - ternary operator
marks = "pass" if marks >=35 else "fail"