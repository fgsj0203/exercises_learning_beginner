"""
Author: Francisco Junior
Date: 04/04/2025 - Brazil format
Description: Provided number in range zero and ten
"""

note = -1  # Condition for require enter loop logical

while (note < 0) or (note > 10):
    note = int(input("note: "))
    if (note < 0) or (note > 10):
        print("Note invalid, try again!")

print("Note final: %d " % note)
