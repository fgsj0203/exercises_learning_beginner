"""
Author: Francisco Junior
Date: 03/04/2025 - Brazil format
Description: Calculate tax based in weight fish
"""

weight_fish = int(input("Weight of fish: "))
value_tax_fish = 4.0

if weight_fish > 50:
    value_final_fish = (weight_fish - 50) * value_tax_fish
    print("The value of tax is: R$ %.1f " % value_final_fish)
else:
    print("You free payment tax")
