# packed args(arguments) - can use variable no of parameters (*variable)
# kwargs - keywords arguments (**variable)

# packed args
"""

def get_grade(*marks):

    total = 0
    for i in marks:
        total += i
    
    print(total)

# function calling
get_grade(78, 45, 99)

"""

# kwargs - keywords arguments 
"""
def my_form(**params):
    
    if 'name' not in params:
        print('Error!')
    else:
        print('Hello '+params['name'])

# function calling
my_form(name='ravindu', height=176, city='panadura')

"""
# packed args first and then kw args

# converting dictionary into a named arguments

def form(name, height):
    print(name, height)

args = {
        'name':'Perera',
        'height':176
    }

form(**args)
