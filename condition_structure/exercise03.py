"""
Author: Francisco Junior
Date: 03/04/2025 - Brazil format
Description: Identify gender based in first letter
"""

gender_identity = str(input("You gender is: f - female or m - male "))
lower_case_gender = gender_identity[0].lower()  # Converting first letter for lowercase

if lower_case_gender == "f":
    print("Your gender is female")
elif lower_case_gender == "m":
    print("Your gender is male")
else:
    print("Gender invalid")
