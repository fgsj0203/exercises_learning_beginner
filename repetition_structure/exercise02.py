"""
Author: Francisco Junior
Date: 04/04/2025 - Brazil format
Description: Provided login and passowrd not equals for valid
"""

login = password = ""

while login == password:
    login = str(input("login: "))
    password = str(input("password: "))
    if login == password:
        print("Login and password is equals, try again!")

print("Login final: %s " % (login))
print("Password final: %s " % (password))
