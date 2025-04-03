"""
Author: Francisco Junior
Date: 03/04/2025 - Brazil format
Description: Calculate weight ideal for people
"""

height_people = float(input("What you height: "))
height_ideal = (72.7 * height_people) - 58

print("Weight ideal for people is %.1f kg" % height_ideal)
