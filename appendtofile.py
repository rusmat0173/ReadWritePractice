""" append to a file, etc.

    This later version tests the def main() way of getting around some plylint issues.
    See Impractical Python Projects, location 582.

""" 
# test commnet of over 79 characters for plint to pcik up 00000000000000000000000000000000000000000000000000000 00000000000000000000000000000000 0000000000000
def main():
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

if __name__ == '__main__':
    main()