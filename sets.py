# sets - unordered, unindex collection, no duplicate values

utensils = {'fork', 'spoon', 'knife'}
dishes = {'bowl', 'plate', 'cup'}
dinnerTable = utensils.union(dishes) # gathered 2 sets and created a new set

# set methods (functions)
utensils.add('grater') # add set items
utensils.remove('fork') # remove set items
utensils.clear() # clear set items
dishes.update(utensils)

print(dishes.difference(utensils)) # dishes have but utensils doesnt
print(utensils.difference(dishes)) # utensils have but dishes doesnt

print(utensils.intersection(dishes)) # both utensils and dishes got

# not set 