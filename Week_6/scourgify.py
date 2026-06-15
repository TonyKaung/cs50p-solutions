import sys
import csv

def main():
    # check for number of command-line arguments and file type
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit()
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit()
    elif not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        # read the file and create another one for updated version
        with open(sys.argv[1]) as read_file, open(sys.argv[2], "w", newline="") as write_file:
            reader = csv.DictReader(read_file)
            writer = csv.DictWriter(write_file, fieldnames=["first_name", "last_name", "house"])
            writer.writeheader()
            # split the names into first and last and write to new file
            for row in reader:
                last_name, first_name = row["name"].split(", ")
                writer.writerow({"first_name": first_name, "last_name": last_name, "house": row["house"]})

    except FileNotFoundError:
        sys.exit("Could not read file")

if __name__ == "__main__":
    main()
                
