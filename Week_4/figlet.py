from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

# check the number of command-line arguments
if len(sys.argv) == 1:
    # if no font is specified, choose a random font
    f = random.choice(figlet.getFonts())
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    # if a font is specified, use it
    f = sys.argv[2]
    # check font validity
    if f not in figlet.getFonts():
        print("Invalid font")
        sys.exit()
    else:
        figlet.setFont(font=f)
else:
    print("Invalid usage")
    sys.exit()

u_input = input("Input: ")
print("Output:", figlet.renderText(u_input))