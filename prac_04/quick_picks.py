"""
CP5632 Practical 4

Program to ask the user for a number of quick picks and display each quick
pick in a new line.
"""

import random


def main():
    NUMBERS = list(range(1, 46))
    quick_picks_num = int(input("How many quick picks? "))
    for i in range(quick_picks_num):
        quick_picks = generate_quick_picks(NUMBERS)
        for quick_pick in quick_picks:
            print("{:>2}".format(quick_pick), end=" ")
        print("")


def generate_quick_picks(NUMBERS):
    """Generate unique quick picks from a list of numbers"""
    quick_picks = []
    for j in range(6):
        quick_pick = random.choice(NUMBERS)
        while quick_pick in quick_picks:
            quick_pick = random.choice(NUMBERS)
        quick_picks.append(quick_pick)
    return quick_picks


main()
