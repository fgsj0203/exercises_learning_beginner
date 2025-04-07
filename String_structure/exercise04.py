"""
Author: Francisco Junior
Date: 07/04/2025 - Brazil format
Description: Printing and counting amount vowels and space blank
"""

name = str(input("name: "))

spaces_blank_amount = []
vowels_amount = []

for x in name:
    if "AEIOU".find(x.upper()) >= 0:
        vowels_amount += 1
    elif x == " ":
        spaces_blank_amount += 1

print("The value final of amount spaces blank is: ", spaces_blank_amount)
print("The value final of amount vowels is: ", spaces_blank_amount)
