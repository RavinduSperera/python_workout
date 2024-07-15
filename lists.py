# food = 'pizza'  a variable
food = ['pizza', 'Burger', 'Pasta', 'Hotdogs'] # baam a list 

# changing elements
food[0] = 'rice & curry'

# list functions
food.append('ice-cream') # add items to the list
food.remove('rice & curry') # remove items
food.pop() # remove the last item of the list
food.insert(0, 'Cake') # add items into different positions of the list
food.sort() # sorting into alphabetical order
food.clear() # completely clear the list

# print(food[0]) - printing elements one by one (inside the [index no])

# print all the elements inthe list
for x in food:
    print(x)