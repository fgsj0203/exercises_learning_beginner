"""
Author: Francisco Junior
Date: 03/04/2025 - Brazil format
Description: Calculate weight ideal based in gender
"""

height_people = float(input("What you height: "))
weight_man_ideal = (72.7 * height_people) - 58
weight_women_ideal = (62.1 * height_people) - 44.7

print("Weight ideal for man %.2f kg" % weight_man_ideal)
print("Weight ideal for women %.2f kg" % weight_women_ideal)
