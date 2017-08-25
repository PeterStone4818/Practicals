""" author : Peter Stone"""

COLOUR_AND_CODE = {"darkslateblue": "#483d8b", "darksalmon": "#e9967a", "darkseagreen": "#8fbc8f",
                   "darkviolet": "#9400d3", "darkslategray": "#2f4f4f", "firebrick": "#b22222",
                   "floralwhite": "#fffaf0", "gainsboro": "#dcdcdc", "forestgreen": "#228b22",
                   "greenyellow": "#adff2f"}
# print(STATE_NAMES)

colour = input("Enter color name with no spaces please: ")
while colour != "":
    if colour in COLOUR_AND_CODE:
        print(colour, "is", COLOUR_AND_CODE[colour.lower()])
    else:
        print("Invalid colour")
    colour = input("Enter color name in with no spaces please: ")
    for key in COLOUR_AND_CODE:
        print("{} {:>2} {}".format(COLOUR_AND_CODE[key], "is", [key]))
