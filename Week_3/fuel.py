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
        if x > y:
            raise ValueError
        z = round(x / y * 100)
        if z <= 1:
            print("E")
        elif z >= 99:
            print("F")
        else:
            print(f"{z}%")
        return True
    except (ValueError, ZeroDivisionError):
        return False

main()