"""
CP1404/CP5632 - Practical
Loops
"""

# Displays all of the odd numbers between 1 and 20 with a space between each one
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c
number_of_stars = int(input("Number of stars: "))
print('*' * number_of_stars)

# d
for i in range(1, number_of_stars + 1):
    print('*' * i)
print()
