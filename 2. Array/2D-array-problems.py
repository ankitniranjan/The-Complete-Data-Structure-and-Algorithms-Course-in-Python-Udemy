#!/usr/bin/env python3

import numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5],
                      [12, 17, 12, 8], [15, 18, 14, 9]])
print(twoDArray)

# Insertion
# 1.1 Adding Column At Beginning
newTwoDArray = np.insert(twoDArray, 0, [[1, 2, 3, 4]], axis=1)
print(newTwoDArray)

# 1.2 Adding Column As 2nd Column
newTwoDArray = np.insert(twoDArray, 1, [[1, 2, 3, 4]], axis=1)
print(newTwoDArray)

# 2.1 Adding Row At Beginning
newTwoDArray = np.insert(twoDArray, 0, [[1, 2, 3, 4]], axis=0)
print(newTwoDArray)

# 2.2 Adding Column As 2nd Row
newTwoDArray = np.insert(twoDArray, 1, [[1, 2, 3, 4]], axis=0)
print(newTwoDArray)

# Output

[[11 15 10  6]
 [10 14 11  5]
 [12 17 12  8]
 [15 18 14  9]]
[[ 1 11 15 10  6]
 [ 2 10 14 11  5]
 [ 3 12 17 12  8]
 [ 4 15 18 14  9]]
[[11  1 15 10  6]
 [10  2 14 11  5]
 [12  3 17 12  8]
 [15  4 18 14  9]]
[[ 1  2  3  4]
 [11 15 10  6]
 [10 14 11  5]
 [12 17 12  8]
 [15 18 14  9]]
[[11 15 10  6]
 [ 1  2  3  4]
 [10 14 11  5]
 [12 17 12  8]
 [15 18 14  9]]

# Accessing an element
def accessElement(array, rowIndex, colIndex):
    if rowIndex >= len(array) and colIndex >= len(array[0]):
        print("Incorrect Index")
    else:
        print(array[rowIndex][colIndex])

# 3rd row 2nd col
accessElement(twoDArray, 2, 1)

#Output
[[11 15 10  6]
 [10 14 11  5]
 [12 17 12  8]
 [15 18 14  9]]
17

# Traversing
def traverse2DArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j], end=" ")
    print()


traverse2DArray(twoDArray)

# Output
11 15 10 6 10 14 11 5 12 17 12 8 15 18 14 9 

# Searching for an element
def search2DArray(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return 'The value is located at index {' + str(i) + ',' + str(j) + '}'
    return 'The element is not found'


print(search2DArray(twoDArray, 14))
print(search2DArray(twoDArray, 24))

#Output
The value is located at index {1,1}
The element is not found

# Deletion of an element
# 1. Delete a row
new2DArray = np.delete(twoDArray, 0, axis=0)
print(new2DArray)

# 1. Delete a column
new2DArray = np.delete(twoDArray, 0, axis=1)
print(new2DArray)

# Output
[[11 15 10  6]
 [10 14 11  5]
 [12 17 12  8]
 [15 18 14  9]]
[[10 14 11  5]
 [12 17 12  8]
 [15 18 14  9]]
[[15 10  6]
 [14 11  5]
 [17 12  8]
 [18 14  9]]
