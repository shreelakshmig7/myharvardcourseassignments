import sys
from pyfiglet import Figlet
import random

def validate_cmdl_arguments(figlet):
    font_type = ""
    fonts_lib = figlet.getFonts()

    if len(sys.argv) == 1:
        font_type = random.choice(fonts_lib)
    elif len(sys.argv) == 3:
        if sys.argv[1] != "-f" and sys.argv[1] != "--font":
            sys.exit("Invalid usage")
        elif sys.argv[2] not in fonts_lib:
            sys.exit("Invalid Font Type")
        else:
            font_type = sys.argv[2]
    else:
        sys.exit("Invalid usage")

    return font_type


def format_output(figlet, font_type, inpt_str):
    figlet.setFont(font=font_type)
    print(figlet.renderText(inpt_str))


def main():
    figlet = Figlet()
    font_type = validate_cmdl_arguments(figlet)
    in_str = input("Input: ")
    format_output(figlet, font_type, in_str)



if __name__ == "__main__":
    main()
