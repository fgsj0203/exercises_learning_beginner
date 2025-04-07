"""
Author: Francisco Junior
Date: 07/04/2025 - Brazil format
Description: Identify if strings if palindrome
"""

name = str(input("name: "))
reverse_name = name[::-1]

if (name.replace(" ", "")) == reverse_name.replace(" ", ""):
    print("The string is palindrome")
else:
    print("The string is not palindrome")
