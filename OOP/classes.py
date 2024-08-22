# python classes
class Dog:
    # pass - continuing without any implimentation 
    # adding propaties
    name = 'Jack'
    breed = 'Beagle'

    # declaring actions
    def bark(self, message): # by default argument - self
        print('Woof Woof!!'+ message)

"""# creating an object 
dog1 = Dog()
dog1.name = 'Scooby'
dog1.breed = 'Unknown'

# created an object in DOg class
dog2 = Dog()
dog2.bark() # method calling 

# prints object 1 stuff
print('Name: ' + dog1.name)
print('Breed: ' + dog1.breed)

# prints onject 2 stuff
print("Name: " + dog2.name)
print('Breed: ' + dog2.breed)"""

dog1 = Dog()
dog1.bark(" Hello!")

dog2 = Dog()
dog2.bark(" Hi!")
