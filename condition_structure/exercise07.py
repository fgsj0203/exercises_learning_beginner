"""
Author: Francisco Junior
Date: 03/04/2025 - Brazil format
Description: Identify bigger and smaller of three numbers
"""

number_one = int(input("number one: "))
number_two = int(input("number two: "))
number_three = int(input("number three: "))

if (number_one == number_two) and (number_one == number_three):
    print("Three numbers is equals")
else:
    if (number_one > number_two) and (number_one > number_three):
        print("The bigger number is one : %d" % number_one)
    elif number_two > number_three:
        print("The bigger number is two : %d" % number_two)
    else:
        print("The bigger number is three : %d" % number_three)

    if (number_one < number_two) and (number_one < number_three):
        print("The smaller number is one : %d" % number_one)
    elif number_two < number_three:
        print("The smaller number is two : %d" % number_two)
    else:
        print("The smaller number is three : %d" % number_three)
