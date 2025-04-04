"""
Author: Francisco Junior
Date: 04/04/2025 - Brazil format
Description: Validating data personal
"""

# Validation of size name
name = str(input("Enter with name: "))
size_name = len(name)
while size_name <= 3:
    print("Name invalid, try again!")
    name = str(input("Enter again with name: "))
    size_name = len(name)
    if size_name <= 3:
        print("Name require most three characters")

# Validation of age people
age = -1
while (age < 0) or (age > 150):
    age = int(input("Enter with you age: "))
    if (age < 0) or (age > 150):
        print("Age invalid, try again!!")

# Validation of salary
salary = 0
while salary <= 0:
    salary = float(input("Enter with you salary: "))
    if salary <= 0:
        print("Salary invalid, try again!!")

# Validation of gender
gender = ""
while (gender != "f") and (gender != "m"):
    gender = str(input("Enter with you gender: "))
    if (gender != "f") and (gender != "m"):
        print("Gender invalid, try again!")

# Validation state civil
state_civil = str(input("Enter with you state civil: "))
while (
    (state_civil != "s")
    and (state_civil != "c")
    and (state_civil != "v")
    and (state_civil != "d")
):
    print("State civil invalid, try again!!")
    state_civil = str(input("Enter with you state civil: "))
