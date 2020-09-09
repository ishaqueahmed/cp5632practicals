"""
CP5632 Practical 5

State names in a dictionary (file has been reformatted)
"""


ABBREVIATION_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales",
                "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory",
                "VIC": "Victoria", "TAS": "Tasmania"}
print(ABBREVIATION_TO_NAME)

state_abbreviation = input("Enter short state: ").upper()
while state_abbreviation != "":
    if state_abbreviation in ABBREVIATION_TO_NAME:
        print(state_abbreviation, "is", ABBREVIATION_TO_NAME[state_abbreviation])
    else:
        print("Invalid short state")
    state_abbreviation = input("Enter short state: ").upper()

print()
for state_abbreviation in ABBREVIATION_TO_NAME:
    print("{:<3} is {:<}".format(state_abbreviation, ABBREVIATION_TO_NAME[state_abbreviation]))
