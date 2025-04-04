"""
Author: Francisco Junior
Date: 04/04/2025 - Brazil format
Description: identify and counter numbers odd and pair
"""

counter_pair = 0
counter_odd = 0
for x in range(0, 10):
    number = int(input("number: "))
    if number % 2 == 0:
        counter_pair += 1
    else:
        counter_odd += 1

print("Amount numbers pair: %d" % counter_pair)
print("Amount numbers odd: %d " % counter_odd)
