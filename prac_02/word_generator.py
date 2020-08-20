"""
CP5632 Practical 2

Program to generate random words based on word format provided by the user.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

word_format = str(input("Enter the word format (% for consonants, # for vowels): ")).lower()
word = ""
for kind in word_format:
    if kind == "%":
        word += random.choice(CONSONANTS)
    elif kind == "#":
        word += random.choice(VOWELS)
    else:
        word += kind

print(word)
