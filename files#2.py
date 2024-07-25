# contex_managers
# with open() as file:
# in here we not gonna need a file.close()

with open('file#2.txt', 'a') as file:
    x = [str(i) for i in range(0, 100)]
    msg = '\n'.join(x)
    file.write(msg)