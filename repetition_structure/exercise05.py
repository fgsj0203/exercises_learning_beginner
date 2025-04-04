"""
Author: Francisco Junior
Date: 04/04/2025 - Brazil format
Description: Returning bigger number of five numbers
"""

big_number = 0
for x in range(0, 5):
    number = int(input("number: "))
    if number > big_number:
        big_number = number
print("The bigger number is: %d " % big_number)
