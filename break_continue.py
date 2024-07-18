count = 0

phone_number = '123-234-4567'

# contiue - skip an item
for i in phone_number:
    if i == '-':
        continue
    print(i, end='')

# into a while loop 
while True:
    print("Count: "+str(count))
    count += 3 # incrementing while looping

    if count >= 10:
        break