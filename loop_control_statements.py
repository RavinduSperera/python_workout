# break - terminating the loop entirely
# continue - slip to the next iteration of the loop
# pass - does nothing, acts as a placeholder - skip things

# break
while True:
    name = input('Enter your name: ')
    if name != '':
        break

# continue
phone_number = '123-345-3456'

for i in phone_number:
    if i == '-':
        continue
    print(i, end='') # end='' - making verticle line horizontal

# pass
for i in range(10, 21):
    if i == 15:
        pass
    else:
        print(i)
