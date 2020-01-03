""" opens a file called food.txt """
divider = " = = = "
f = open("food.txt", "r")
data = f.read()
print(data)
f.close()

print(divider)

""" using with allows you to open and close file in one go """
with open("food.txt", "r") as f:
    for line in f:
        print(line)