def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    if 2 > len(plate) or len(plate) > 6:
        return False
    if not plate[0:2].isalpha():
        return False
    for i in range(len(plate)):
        if not plate[i].isalpha() and not plate[i].isdigit():
            return False
    seen_number = False
    for i in range(2, len(plate)):
        if plate[i].isdigit() and plate[i] == "0" and not seen_number:
            return False
        elif plate[i].isdigit() and not seen_number:
            seen_number = True
        elif plate[i].isalpha() and seen_number:
            return False
    return True

main()
            