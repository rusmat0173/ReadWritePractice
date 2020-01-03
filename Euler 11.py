""" Enjoyed this Euler project Q11, as quite a few things to think about.
    Aim is to take a 20x20 matrix of numbers and find out which product of
    four consecutive numbers is th highest, horizontally, vertically or diagonally.

    Broken into several stages:
    i. Cut and paste matrix from Euler website into Excel spreasdsheet and save as "raw_matrix.csv".
    ii. Read-in raw_matrix.csv and change each row from a list with a single string to a list with multiple strings,
    delineated by commas.  Keep 'numbers' as string objects as you can then do better stuff later on,
    such as printing some numbers in colour.
    iii. Create a row-reading highest product engine, that saves highest product and position of the four terms.
    N.B. Keeps 'terms' as strings at the end.
    iv. Create a similar diagonal-reading highest product engine, that will work starting always on first row.
    (Diagonals will be different lengths.)  That means ~half of diagonals are not read.  (Those in bottom left.)
    N.B. Keeps 'terms' as strings at the end.
    v. Create a transpose matrix function:
    > Means you can use the row-reading engine to check highest product of columns,
    > Means you can use the diagonal-reading engine to check highest product of the bottom half of diagonals.
    vi. Have not yet checked diagonals that run from top right to bottom left. This can be achieved
    by doing a horizontal reflection on the original matrix and then using the diagonal-reading engine.
"""
import csv
import copy
# ^ this is needed to change matrices, but keep originals

# step i.
# read csv file. Output is a list of lists, with the element lists containing a single string of character numbers.
def read_file(csv_file):
    with open(csv_file, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        # get all the rows as a list
        data = list(reader)
    return data

# step ii.
# function to take a list with single string of characters, to list of multiple string of characters
# by inspection, this works as every 'string number' is two characters long, makes much simpler
def one_to_many(a_list):
    for single_str in a_list:
        output = []
        dummy_str = ''
        for i in range(len(single_str)):
            if single_str[i] != ' ':
               dummy_str += single_str[i]
            if i == (len(single_str) - 1) or single_str[i] == ' ':
                output.append(dummy_str)
                dummy_str = ''

    return output

# function to iterate through rows of csv file and output to a new matrix that will be the one we use
def create_matrix(a_list):
    new_matrix = []
    for row in a_list:
        new_matrix.append(one_to_many(row))
    return new_matrix

# step iii.  function returns row's highest product and start index of sequence as a tuple
def horizontal_product_engine(a_row):
    order = len(a_row)
    highest_product = 0
    for i in range(order -3):
        product = int(a_row[i])
        for j in range(1,4):
            product *= int(a_row[i+j])
        if product > highest_product:
            highest_product = product
            start_index = i
    return start_index, highest_product

# step iv. function returns matrix's highest product and start index , for top right 'triangular' half
def diagonal_product_engine(a_matrix):
    order = len(a_matrix)
    highest_product = 0
    index = [0,0]
    for i in range(order -3):
        for j in range(order - i - 3):
            product = int(a_matrix[j][i+j])
            for k in range(1,4):
                product *= int(a_matrix[j+k][i+j+k])
            if product > highest_product:
                highest_product = product
                index = [j, j+i]

    return index, highest_product

# step v. function transposes the square matrix
def transpose(matrix):
    b_matrix = copy.deepcopy(matrix)
    order = len(b_matrix[0])
    for i in range(order):
        for j in range(order):
            if j > i:
                temp = b_matrix[i][j]
                b_matrix[i][j] = b_matrix[j][i]
                b_matrix[j][i] = temp
    return b_matrix

# step vi. function to reflect a square matrix about a vertical axis
# since 'centre' row element in odd-number 'order' doesn't move,
# we always swap elements up to the order//2-th element
def reflect(matrix):
    b_matrix = copy.deepcopy(matrix)
    order = len(matrix[0])
    for i in range(order):
        for j in range(order//2):
                temp = b_matrix[i][j]
                b_matrix[i][j] = b_matrix[i][order-1-j]
                b_matrix[i][order-1-j] = temp

    return b_matrix


# = = = = = = =
# create working matrices
raw_matrix = read_file('raw_matrix.csv')
base_matrix = create_matrix(raw_matrix)

# find highest product of all rows
highest_row = 0
start_index = 0
max_product = 0
counter = 0
for row in base_matrix:
    index_product = horizontal_product_engine(row)
    if index_product[1] > max_product:
        max_product = index_product[1]
        highest_row = counter
        start_index = index_product[0]
    counter += 1
print('For rows: Start index is: [{}, {}], Highest product is: {}'.format(highest_row, start_index, max_product))

# find highest product of top diagonals (top left to bottom right)
a = diagonal_product_engine(base_matrix)
print('For initial diagonals: Start index is {}, Highest Product is:{}'.format(a[0], a[1]))

# transpose matrix to find highest product of columns and bottom diagonals ((top left to bottom right)
transpose_matrix = transpose(base_matrix)
# find highest product of all rows
highest_row = 0
start_index = 0
max_product = 0
counter = 0
for row in transpose_matrix:
    index_product = horizontal_product_engine(row)
    if index_product[1] > max_product:
        max_product = index_product[1]
        highest_row = counter
        start_index = index_product[0]
    counter += 1
# when printing out, swap start indices to match original matrix
print('For Columns: Start index is: [{}, {}], Highest product is: {}'.format(start_index, highest_row, max_product))

# then bottom diagonals:
a = diagonal_product_engine(transpose_matrix)
# need to swap indices to match original matrix
b =[a[0][1], a[0][0]]
print('For second diagonals: Start index is {}, Highest Product is:{}'.format(b, a[1]))

# next, need to do diagonals, bottom left to top right
# done by original matrix, them transpose, then reflect
reflect_transpose_matrix =  reflect(transpose_matrix)
rfm = reflect_transpose_matrix

# find highest product of top diagonals (top left to bottom right)
c = diagonal_product_engine(rfm)
# not sure these start indices are good, versus original matrix, BTW
print('For third diagonals: Start index is {}, Highest Product is:{}'.format(c[0], c[1]))

# find highest product of bottom diagonals (top left to bottom right),
# need to get original matrix and then reflect, transpose, reflect
reflect_matrix= reflect(base_matrix)
transpose_reflect_matrix = transpose(reflect_matrix)
reflect_transpose_reflect_matrix = reflect(transpose_reflect_matrix)
rtr = reflect_transpose_reflect_matrix
d = diagonal_product_engine(rtr)
# not sure these start indices are good, versus original matrix, BTW
print('For fourth diagonals: Start index is {}, Highest Product is:{}'.format(d[0], d[1]))

""" My answer of 70600674 is correct, yeah!  
    What a great puzzle for thinking through lots of stuff:
    deepcopy, and how I accidently kept changing the base matrix!
    elegant code
    making calculation engines: how to deal with reaching the end of a row
    complex, for me, iterations through i, j, k, and order 
    reflecting and transposing
    manipulating immutable strings in lists
    reading csv, especially as header row never came. (There's some header parameter/command)
    Basically took a whole day equivalent
    
    What did I like: that I broke down problem into steps and coded functions for the steps.
    However, if you look at the Euler thread for this problem, some people did this in just a few lines of code!!!
    (e.g. look particularly at Silverfish, 18 Feb 2006, 10:59)
    
"""



