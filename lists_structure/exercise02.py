"""
Author: Francisco Junior
Date: 04/04/2025 - Brazil format
Description: Creating list with numbers and printing in order reverse
"""

# list empty numbers
list_numbers = []

for x in range(0, 5):
    number = int(input("number: "))
    list_numbers.append(number)

# Printing list of numbers reverse and in order
print("The list numbers: ", list_numbers)
print("The list numbers reverse: ", list_numbers[::-1])
