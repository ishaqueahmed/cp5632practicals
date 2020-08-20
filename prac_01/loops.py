"""
CP5632 Practical 1

Loops for displaying odd numbers between 1 and 20, counting in 10s from 1 to
100, counting down from 20 to 1, and displaying stars based on user input
"""

for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

stars = int(input("Number of stars: "))
for i in range(1, stars + 1):
    print("*", end="")
print()

stars = int(input("Number of stars: "))
for i in range(1, stars + 1):
    for j in range(1, i+1):
        print("*", end="")
    print()
