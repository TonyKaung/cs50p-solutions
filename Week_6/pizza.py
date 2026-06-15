import csv
import sys
from tabulate import tabulate

def main():
    # check for number of command-line arguments and file type
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit()
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit()
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    
    try:
        # read the file
        with open(sys.argv[1]) as read_file:
            reader = csv.reader(read_file)
            # print the grid menu
            print(tabulate(reader, headers="firstrow", tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()