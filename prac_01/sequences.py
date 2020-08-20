"""
CP5632 Practical 1

Program to display even numbers, odd numbers and squares between x and y
provided by the user.
"""

x = int(input("Enter value of x: "))
y = int(input("Enter value of y: "))

print("\nEven numbers: ")
for i in range(x, y, 2):
    if i % 2 == 0:
        print(i, end=" ")
    else:
        print(i + 1, end=" ")

print("\nOdd numbers: ")
for i in range(x, y, 2):
    if i % 2 == 0:
        print(i + 1, end=" ")
    else:
        print(i, end=" ")

print("\nSquares: ")
for i in range(x, y + 1):
    if (i ** 0.5).is_integer():
        print(i, end=" ")

print()



