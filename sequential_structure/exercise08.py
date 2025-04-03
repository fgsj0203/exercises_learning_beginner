"""
Author: Francisco Junior
Date: 03/04/2025 - Brazil format
Description: Calculate salary brute in month
"""

value_hour_work = float(input("value hour work in month: "))
hours_worked_month = int(input("What hours worked in month: "))

salary_brute = value_hour_work * hours_worked_month
print("The salary brute is R$ %.2f " % salary_brute)
