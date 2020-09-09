"""
CP5632 Practical 5

Program to ask the user for colour name and then display the respective colour code
"""

COLOUR_CODES = {"aliceblue": "#f0f8ff",
               "antiquewhite": "#faebd7",
               "blanchedalmond": "#ffebcd",
               "blueviolet": "#8a2be2",
               "cadetblue": "#5f9ea0",
               "cornflowerblue": "#6495ed",
               "darkgoldenrod": "#b8860b",
               "darkgreen": "#006400",
               "darkkhaki": "#bdb76b",
               "darkolivegreen": "#556b2f"}

colour_name = input("Enter a colour name: ")
while colour_name != "":
    if colour_name.lower() in COLOUR_CODES:
        print("Colour code is {}".format(COLOUR_CODES[colour_name.lower()]))
    else:
        print("Colour name not in dictionary")
    colour_name = input("Enter a colour name: ")
