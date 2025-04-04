"""
Author: Francisco Junior
Date: 04/04/2025 - Brazil format
Description: return sum of five numbers and average
"""

sum = 0
for x in range(0, 5):
    number = int(input("number: "))
    sum += number

# calculating average
average_numbers = sum / 5

print("Sum of numbers is: %d " % sum)
print("The average of numbers is: %d " % average_numbers)
