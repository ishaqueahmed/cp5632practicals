"""
CP5632 Practical 3

Ask the user for the number of scores to generate randomly and add the
results to results.txt
"""

import random


def main():
    scores_count = int(input("Enter number of scores to generate randomly: "))
    file = open("results.txt", "w")
    for i in range(0, scores_count):
        score = random.randint(0, 100)
        status = determine_status(score)
        file.write("{} is {}\n".format(score, status))


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
