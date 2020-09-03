"""
CP5632 Practical 4

Program to get 5 numbers from user, append them to a list and display first
number, last number, smallest number, largest number and average of the numbers
"""


def main():
    numbers = []
    for i in range(0, 5):
        number = int(input("Number: "))
        numbers.append(number)

    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    print("The average of the numbers is {}".format(sum(numbers)/len(numbers)))


main()
