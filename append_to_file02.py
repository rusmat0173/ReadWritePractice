""" append to a file, etc."""

f = open("second_file.txt", "w")

name = input('Hello, please give your name. ')
print('Hello ' + name)
f.write(name)
f.close()

f = open("second_file.txt", "a")
middle_name = input('Middle name, please. ')
print('Hello {} {}'.format(name, middle_name))
f.write("\n" + middle_name )
f.close()