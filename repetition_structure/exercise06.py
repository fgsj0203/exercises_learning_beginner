"""
Author: Francisco Junior
Date: 04/04/2025 - Brazil format
Description: return sum of five numbers and average
"""

sum_numbers = 0
for x in range(0, 5):
    number = int(input("number: "))
    sum_numbers += number

# calculating average
average_numbers = sum_numbers / 5

print("Sum of numbers is: %d " % sum_numbers)
print("The average of numbers is: %d " % average_numbers)
