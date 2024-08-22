# self parameter / argument 
class Dog:
    # declarign properties
    name = ''
    breed = ''

    # declaring actions
    def set_name(self, name):
        self.name = name
    
    def bark(self, message):
        msg = f'woof woof My name is {self.name}. {message}' # using string formatting stuff
        print(msg)

    def walk(self):
        print('Walking...')

# creating an object usign Dog class 
dog1 = Dog()
dog1.set_name('Scooby')
dog1.bark(' Hi')

# creating another object using Dog class 
dog2 = Dog()
dog2.set_name("Goofy")
dog2.bark(' Hello')