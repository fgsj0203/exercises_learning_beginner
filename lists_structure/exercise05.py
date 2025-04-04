"""
Author: Francisco Junior
Date: 04/04/2025 - Brazil format
Description: separate numbers of odd and pair
"""

list_numbers = []
list_pair = []
list_odd = []

for x in range(0, 5):
    number = int(input("number: "))
    if number % 2 == 0:
        list_pair.append(number)
    else:
        list_odd.append(number)
    list_numbers.append(number)

print("List of numbers: ", list_numbers)
print("List of numbers pair: ", list_pair)
print("List of numbers odd: ", list_odd)
