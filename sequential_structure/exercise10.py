"""
Author: Francisco Junior
Date: 03/04/2025 - Brazil format
Description: Printing values in three operations mathematical
"""

number_one = int(input("number one: "))
number_two = int(input("number two: "))
number_three = float(input("number three: "))

# Section of calculate operations
operation_one = (number_one * 2) / (number_two / 2)
operation_two = (number_one * 3) + number_three
operation_three = number_three**2

print("Operation one: %.1f " % operation_one)
print("operation two: %.1f " % operation_two)
print("Operation three: %.1f " % operation_three)
