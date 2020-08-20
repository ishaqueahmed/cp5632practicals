"""
CP5632 Practical 1

Program to calculate the total price of items based on the number of items
and the price of each item provided by the user.
"""

number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

total_price = 0

for item in range(0, number_of_items):
    item_price = float(input("Price of item: "))
    total_price += item_price

if total_price > 100:
    total_price = total_price * 0.9

print("Total price for {} items is ${:.2f}".format(number_of_items, total_price))
