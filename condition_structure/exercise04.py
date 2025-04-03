"""
Author: Francisco Junior
Date: 03/04/2025 - Brazil format
Description: Identify and find letter if vowel or consonant
"""

letter = str(input("Letter: "))
letter_lower = letter.lower()
if (
    letter != "a"
    and letter != "e"
    and letter != "i"
    and letter != "o"
    and letter != "u"
):
    print("Letter is consonant")
else:
    print("Letter is vowel")
