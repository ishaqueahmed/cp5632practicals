"""
CP5632 Practical 1

Debugged version of program to determine score status
"""

import random


def main():
    score = float(input("Enter score: "))
    status = determine_status(score)
    print(status)

    score = random.randint(0, 100)
    print("\nRandom score: {}".format(score))
    status = determine_status(score)
    print(status)


def determine_status(score):
    """Determine the status of a score"""
    if score > 100:
        status = "Invalid score"
    elif score >= 90:
        status = "Excellent"
    elif score >= 50:
        status = "Passable"
    elif score >= 0:
        status = "Bad"
    else:
        status = "Invalid score"
    return status


main()
