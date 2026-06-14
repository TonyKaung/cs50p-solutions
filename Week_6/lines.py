import sys

def main():
    # check for number of command-line arguments
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit()
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit()

    count = 0
    with open(sys.argv[1]) as read_file:
        # go through each line and skip comments and blank lines
        for line in read_file:
            line = line.strip()
            if line and not line.startswith("#"):
                count += 1
    print(count)

if __name__ == "__main__":
    main()