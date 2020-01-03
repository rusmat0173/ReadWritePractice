""" Trying to improve the Euler Q11 that I did, using techniques/ideas from the
    Project Euler forum for that question.

    We SAVE A LOT OF TIME compared to before by using f.read().splitline()
    <= that creates lists with a string inside,
    rather than a single huge string, and row.split(),
    that turns each string into a list of integers

"""
with open("Euler11.txt", "r") as f:
    data = f.read().splitlines()

# this is much shorter than before, and uses the split method on a string
# new_matrix = []
# for row in data:
#     temp = []
#     x = (row.split())
#     for y in x:
#         temp.append(int(y))
#     new_matrix.append(temp)
# print(new_matrix)

# this is even shorter, and very beautiful, with a list comprehension to generate the list! (Not thought of by me, sadly.)
# It is effectively the same as my method above, but combines open file and creating matrix together.
with open("Euler11.txt", "r") as data:
    W = []
    for row in data:
        W.append([int(x) for x in row.split()])
# print(W)

order = len(W)
consecutive = 4
max_product = 0
# check horizontal
for i in range(order):
    for j in range(order - consecutive):
        product = 1
        for k in range(j, j+consecutive):
            product *= W[i][k]
        if product > max_product:
            max_product = product

# check vertical
for j in range(order):
    for i in range(order - consecutive):
        product = 1
        for k in range(i, i+consecutive):
            product *= W[k][j]
        if product > max_product:
            max_product = product

# check se-running diagonals
for j in range(order-consecutive + 1):
    for i in range(order - consecutive + 1):
        product = 1
        for k in range(consecutive):
            product *= W[i+k][j+k]

        if product > max_product:
            max_product = product

# check ne-running diagonals
for i in range(consecutive-1, order):
    for j in range(order - consecutive+1):
        product = 1
        for k in range(consecutive):
            product *= W[i-k][j+k]
        if product > max_product:
            max_product = product

print(max_product)




