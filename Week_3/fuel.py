def main():
    while True:
        u_input = input("Fraction: ")
        if fuel(u_input):
            break

def fuel(u_input):
    try:
        x, y = u_input.split("/")
        x = int(x)
        y = int(y)
        z = round (x/y * 100)
        if z < 0 or z > 100:
            raise ValueError
        elif z <= 1:
            print("E")
        elif z >= 99:
            print("F")
    except(ValueError, ZeroDivisionError):
        print("Invalid input")
        return False
    else:
        print(f"{z}%")
        return True

main()