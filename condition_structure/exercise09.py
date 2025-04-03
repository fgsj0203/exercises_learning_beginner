"""
Author: Francisco Junior
Date: 03/04/2025 - Brazil format
Description: Calculate area of circle
"""

print("[M]-Morning")
print("[A]-Afternoom")
print("[N]-Night")
print("Enter with shift learn: ")
shift_learn = str(input(""))
shift_learn_lower = shift_learn[0].lower()

if shift_learn_lower == "m":
    print("Good Morning")
elif shift_learn_lower == "a":
    print("Good Afternoom")
elif shift_learn_lower == "n":
    print("Good night")
else:
    print("Shift invalid")
