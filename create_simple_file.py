""" create a file, etc."""

f = open('first_file.txt', 'w')

name = input('Hello, please give your name. ')
print('Hello ' + name)

f.write(name)
f.close()