"""
CP5632 Practical 2

Capitalist Conrad program, updated to display day counter, have price range
between $1 and $100, allow price increase upto 17.5% and write to file
output_file.txt
"""
import random

MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
OUTPUT_FILE = "output_file.txt"

price = INITIAL_PRICE
day_count = 0
out_file = open(OUTPUT_FILE, 'w')
print("Starting price: ${:,.2f}".format(price), file=out_file)

while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    day_count += 1
    price *= (1 + price_change)
    print("On day {} price is: ${:,.2f}".format(day_count, price), file=out_file)
out_file.close()
