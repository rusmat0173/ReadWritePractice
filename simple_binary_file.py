divider = " * * * "

data = [100,24,255]
buffer = bytes(data)
print(buffer)
f = open("binary.txt", "bw") # <= mode is binary write
f.write(buffer)
f.close()

print(divider)

# this opens the binary text file and turns back into something we can read
f = open("binary.txt", "br") # <= mode is binary read
binary = f.read()
print(binary)
data = list(binary) # <= this is kind of magic, the "br" mode has turned into readable stuff
print(data)
f.close()