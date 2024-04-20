'''Understanding Assignments and Comparisons'''

#Task 1: Value Swapping. Swap the values of two given numbers using assignment operators (=) and then compare them to ensure they have been swapped.

a = 10
b = 20

c = a
a = b
b = c

print(a > b)
print("Value of a:", a)
print("Value of b:", b)