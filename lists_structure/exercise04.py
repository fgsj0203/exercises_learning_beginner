"""
Author: Francisco Junior
Date: 04/04/2025 - Brazil format
Description: Identify what letter is consonant or vowel
"""

list_letter = []
list_consonant = []
LIST_VOWEL = "aeiou"
counter_consonant = 0

for x in range(0, 5):
    letter = str(input("letter: "))
    if letter not in LIST_VOWEL:
        list_consonant.append(letter)
        counter_consonant += 1

print("The list of consonants is: ", list_consonant)
print("Amount of consonants: ", counter_consonant)
