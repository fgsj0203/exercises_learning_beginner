"""
Author: Francisco Junior
Date: 04/04/2025 - Brazil format
Description: Create list with notes and calculate average value
"""

list_notes = []
for x in range(0, 4):
    note = float(input("note: "))
    list_notes.append(note)
    sum_notes = sum(list_notes)

print("The list of notes: ", list_notes)
print("Average of notes: ", sum_notes / 4)
