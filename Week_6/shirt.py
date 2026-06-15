import sys
from PIL import Image, ImageOps
import os

def main():
    # check for number of command-line arguments and file type
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit()
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit()

    input_file = sys.argv[1].lower()
    output_file = sys.argv[2].lower()

    # get the extensions for the files
    input_ext = os.path.splitext(input_file)[1]
    output_ext = os.path.splitext(output_file)[1]

    # check for valid extensions for the files
    valid_extensions = [".jpg", ".jpeg", ".png"]
    if input_ext not in valid_extensions or output_ext not in valid_extensions:
        sys.exit("Invalid input or output file")

    # check extensions match for the files
    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

    try:
        # open the files
        input_image = Image.open(input_file)
        shirt = Image.open("shirt.png")

        # resize the input image to fit the shirt
        input_image = ImageOps.fit(input_image, shirt.size)

        # put the shirt on top of the input image
        input_image.paste(shirt, shirt)

        # save the new image
        input_image.save(output_file)

    except FileNotFoundError:
        sys.exit("Could not read file")

if __name__ == "__main__":
    main()

