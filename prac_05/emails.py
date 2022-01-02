"""
CP1404/CP5632 Practical
Hexadecimal colour lookup
"""
COLOR_HEX = {
    "Absolute Zero": "#0048ba",
    "Acid Green": "#b0bf1a",
    "Zomp": "#39a78e",
    "Zaffre": "#0014a8",
    "YellowGreen": "#9acd32",
    "Yellow Pantone": "#fedf00",
    "Xanadu": "#738678",
    "Wisteria": "#c9a0dc",
    "Wine": "#722f37",
    "White": "#ffffff"
}

def main():
    """
    The program takes input from the user and returns the corresponding hexadecimal color code.
    """
    color_name = input("Color name: ").strip()
    while color_name != "":
        for key in COLOR_HEX.keys():
            if key.lower() == color_name.lower():
                hex = COLOR_HEX.get(key, "")
                print("The hexadecimal colour codes of color {} is {}".format(color_name, hex))
                break
        color_name = input("Color name: ").strip()


if __name__ == "__main__":
    main()