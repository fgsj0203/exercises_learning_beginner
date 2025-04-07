"""
Author: Francisco Junior
Date: 07/04/2025 - Brazil format
Description: Comparate size and content of two strings
"""

name_one = str(input("name one = "))
name_two = str(input("name two = "))

# Printing of sizes strings

print("The size of name one is: %d " % (len(name_one)))
print("The size of name two is: %d " % (len(name_two)))

# Compare size and content of two strings

if len(name_one) != len(name_two):
    print("The two strings having sizes not equals")
    print("The content of two strings is not equals")
else:
    print("The two strings is size equals")
    if name_one == name_two:
        print("The size having content equals")
    else:
        print("The content is not equals")
