# dictionaries - A changeable, unordered collection of unique key:value pairs
#                fast becaues they use hashing, allow us to access a value quickly

capitals = {'USA':'Washington DC',
            'India':'New Dhilli', 
            'China':'Bejin',
            'Rusia':'Moscow'}

# add a new 
capitals.update(
    {'Germani':'Berlin'}
)

# updating exist one 
capitals.update(
    {'USA':'Las Vegas'}
)

# remove entire item
capitals.pop('China')

# clear entire dictionary
capitals.clear()

print(capitals.get('China')) # spesific one 
print(capitals.keys()) # all the keys
print(capitals.values()) # all the values
print(capitals.items()) # all the items
print('')

# display all without brackets clearly
for key, value in capitals.items():
    print(key, value)