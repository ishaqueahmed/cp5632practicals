"""
CP5632 Practical 2

Write the user's name to name.txt, read from name.txt to display user's name
and add numbers provided in numbers.txt
"""

name = input("Enter your name: ")

file = open("name.txt", "w")
file.write(name)
file.close()

file = open("name.txt", "r")
print("Your name is {}".format(file.read()))
file.close()

file = open("numbers.txt", "r")
num1 = int(file.readline())
num2 = int(file.readline())
print("Sum of first two numbers: {}".format(num1+num2))
file.close()

file = open("numbers.txt", "r")
sum_of_numbers = 0
for line in file:
    sum_of_numbers += int(line)
file.close()
print("Sum of all numbers: {}".format(sum_of_numbers))
