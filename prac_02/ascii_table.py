"""
CP5632 Practical 2

Convert from character to ASCII code and vice versa, and display ASCII table
"""

LOWER_LIMIT = 33
UPPER_LIMIT = 127

character = input("Enter a character: ")
print("The ASCII code for {} is {}".format(character, ord(character)))

ascii_code = int(input("Enter a number between {} and {}: ".format(LOWER_LIMIT, UPPER_LIMIT)))
while ascii_code < LOWER_LIMIT or ascii_code > UPPER_LIMIT:
    print("Number out of range.")
    ascii_code = int(input("Enter a number between {} and {}: ".format(LOWER_LIMIT, UPPER_LIMIT)))
print("The character for {} is {}".format(ascii_code, chr(ascii_code)))

for a in range(LOWER_LIMIT, UPPER_LIMIT + 1):
    print("{:>3}  {}".format(a, chr(a)))
