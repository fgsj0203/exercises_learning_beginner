"""
Author: Francisco Junior
Date: 03/04/2025 - Brazil format
Description: identify bigger of three numbers
"""

number_one = int(input("number one: "))
number_two = int(input("number two: "))
number_three = int(input("number three: "))

if (number_one == number_two) and (number_one == number_three):
    print("numbers is equal")
elif (number_one > number_two) and (number_one > number_three):
    print("number one is bigger! ", number_one)
elif number_two > number_three:
    print("Number two is bigger! ", number_two)
else:
    print("Number three is bigger! ", number_three)
