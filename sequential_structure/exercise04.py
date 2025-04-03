"""
author: Francisco Junior
Date: 03/04/2025 - Brazil format date
Exercise: printing average of four notes school
"""

note_one = float(input("note one: "))
note_two = float(input("note two: "))
note_three = float(input("note three: "))
note_four = float(input("note four: "))

# Calculating average notes of school student
average_notes = (note_one + note_two + note_three + note_four) / 4.0

print("The average note is: %.2f" % average_notes)
