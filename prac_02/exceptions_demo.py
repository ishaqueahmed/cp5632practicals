"""
CP5632 Practical 2

1. When will a ValueError occur?
A: ValueError occurs when inputs given do not have an integer data type,
e.g. float, string, etc.

2. When will a ZeroDivisionError occur?
A: ZeroDivisionError occurs when denominator value provided is 0.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
A: Yes, the code has been modified to prompt the user to enter a different
denominator before calculating the result
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
