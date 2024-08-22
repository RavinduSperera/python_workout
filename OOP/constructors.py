# constructors -
class Dog:

    # constructor 
    def __init__(self, name = 'unknown'):
        self.name = name

    def set_name(self, name):
        self.name = name
    
    def bark(self, message):
        msg = f'Woof Woof, My name is {self.name}. {message}'
        print(msg)
    
    def walk(self):
        print('Walking...')
    
dog1 = Dog('Scooby') # running the constructor here
dog1.bark('Heyy!')

dog2 = Dog() # running the constructor here 
dog2.bark('Hii')