"""
CP5632 Practical 1

Debugged version of program to determine score status
"""

score = float(input("Enter score: "))

if score > 100:
    print("Invalid score")
elif score > 90:
    print("Excellent")
elif score > 50:
    print("Passable")
elif score >= 0:
    print("Bad")
else:
    print("Invalid score")
