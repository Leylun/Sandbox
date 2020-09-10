hex_colours = {
    "aliceblue": "f0f8ff",
    'beige': "f5f5dc",
    'black': "000000",
    'brown': "a52a2a",
    'cadetblue': "5f9ea0",
    'coral': "ff7f50",
    'darkgreen': "006400",
    'darkorchid': "9932cc",
    'dimgray': "696969",
    'firebrick': "b22222",
}
print("Available Colours:")
for item in hex_colours:
    print(item)
given_colour = input("Please choose the colour you wish for hexa-decimal.")
print("Colour: {}, Hexa-Decimal: {}".format(given_colour, hex_colours[given_colour.lower()]))