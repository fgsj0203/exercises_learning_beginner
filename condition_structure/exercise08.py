"""
Author: Francisco Junior
Date: 03/04/2025 - Brazil format
Description: Printing three values in order descending
"""

number_one = int(input("number one: "))
number_two = int(input("number two: "))
number_three = int(input("number three: "))

if (number_one > number_two) and (number_one > number_three):
    print("bigger number %d" % number_one)
    if number_two > number_three:
        print("middle number: %d " % number_two)
        print("smaller number: %d " % number_three)
    else:
        print("middle number: %d " % number_three)
        print("smaller number: %d " % number_two)

elif number_two > number_three:
    print("bigger number: %d " % number_two)
    if number_one > number_three:
        print("middle number: %d" % number_one)
        print("smaller number: %d" % number_three)
    else:
        print("middle number: %d" % number_three)
        print("smaller number: %d " % number_one)

else:
    print("bigger number: %d" % number_three)
    if number_one > number_two:
        print("middle number: %d" % number_one)
        print("smaller number: %d" % number_two)
    else:
        print("middle number: %d" % number_two)
        print("smaller number: %d" % number_one)
