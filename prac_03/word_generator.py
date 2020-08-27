"""
CP5632 Practical 3

Program to generate random words based on word format provided by the user.
"""

import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"


def main():
    word_format = str(input("Enter the word format (c for consonants, v for vowels): ")).lower()
    while not is_valid_format(word_format):
        print("Word format must only contain c's and v's")
        word_format = str(input("Enter the word format (c for consonants, v for vowels): ")).lower()

    word = ""
    for kind in word_format:
        if kind == "c":
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)

    print(word)


def is_valid_format(word_format):
    """Validates the word format"""
    return all(char == "c" or char == "v" for char in word_format)


main()
