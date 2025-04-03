"""
Author: Francisco Junior
Date: 03/04/2025 - Brazil format
Description: Calculate average of two notes student
"""

note_one = float(input("note one: "))
note_two = float(input("note two: "))

average_notes = (note_one + note_two) / 2.0

if average_notes == 10.0:
    print("Approved with distinction")
elif average_notes >= 7.0 and average_notes <= 9.9:
    print("Approved")
else:
    print("Reproved")
