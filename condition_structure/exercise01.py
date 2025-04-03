"""
Author: Francisco Junior
Date: 03/04/2025 - Brazil format
Description: Identify bigger of two numbers
"""

number_one = int(input("number one: "))
number_two = int(input("number two: "))

if number_one > number_two:
    print("The number one is bigger %d " % number_one)
elif number_two > number_one:
    print("The number two is bigger %d " % number_two)
else:
    print("The two numbers is equal")
