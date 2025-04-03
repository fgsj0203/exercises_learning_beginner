"""
Author: Francisco Junior
Date: 03/04/2025 - Brazil format
Description: Calculate area of circle
"""

salary = float(input("salary: "))

if salary <= 280:
    new_salary = salary + (salary * 0.20)
    print("Salary: R$ %.2f" % salary)
    print("20%")
    print("Value increase in salary R$ %.2f " % (salary * 0.20))
    print("Your new salary is: R$ %.2f" % new_salary)

elif salary <= 700:
    new_salary = salary + (salary * 0.15)
    print("Salary: R$ %.2f" % salary)
    print("15%")
    print("Value increase in salary R$ %.2f " % (salary * 0.15))
    print("Your new salary is: R$ %.2f" % new_salary)
elif salary <= 1500:
    new_salary = salary + (salary * 0.10)
    print("Salary: R$ %.2f" % salary)
    print("10%")
    print("Value increase in salary R$ %.2f " % (salary * 0.10))
    print("Your new salary is: R$ %.2f" % new_salary)
else:
    new_salary = salary + (salary * 0.05)
    print("Salary: R$ %.2f" % salary)
    print("5%")
    print("Value increase in salary R$ %.2f " % (salary * 0.05))
    print("Your new salary is: R$ %.2f" % new_salary)
