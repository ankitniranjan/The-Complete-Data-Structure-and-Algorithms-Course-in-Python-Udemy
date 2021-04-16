#!/usr/bin/env python3

from array import *

myArray = array('i', [1, 2, 3, 4, 5])

# Create an array and traverse
for i in myArray:
    print(i, end=" ")
print()

# Access indivisual elements through indexes
for index, ele in enumerate(myArray):
    print(index, ele)

# Append any value to the array using append() method
myArray.append(6)
print(myArray)

# Insert value in the array using insert() method
myArray.insert(0, -1)
print(myArray)

# Extend python array using extend() method
myArray.extend([7, 8, 9])
print(myArray)

# Add items from list into array using fromlist() method
mylist = [10, 20, 30]
myArray.fromlist(mylist)
print(myArray)

# Remove any array element using remove() method
myArray.remove(-1)
print(myArray)

# Remove last array element using pop() method
myArray.pop()
print(myArray)

# Fetch any element through its index using index() method
print("Element at index 5 is = ", myArray.index(5))

# Reverse a python array using reverse() method
myArray.reverse()
print(myArray)

# Get array buffer inforamtion through buffer_info() method
address, length = myArray.buffer_info()
print("Array stored at location = ", address, " Size of array = ", length*4)

# Check for number of occurence of an element using count() method
print(myArray.count(5))

# Convert array to python list with same elements using tolist() method
print(myArray.tolist())

# Append a string to char array using fromstring() method
# sArray = array("b", ["a", "b"])
# string = "Hello"
# print(sArray.fromstring(string))

# Slice elements from an array
print(myArray[2:5])
