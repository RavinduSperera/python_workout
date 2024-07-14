# and , or , not

temp = float(input('Current temp: '))

if temp >=0 and temp <= 30:
    print('the temparature is good today,')
    print('You can enjoy going outside!')

elif temp < 0 or temp > 30:
    print('the temparature is bad today,')
    print('stay inside!')

elif not(temp < 54 and temp < 100): # the not operator
    print('This is not operator')

else: 
    print('Error!')