def convert(string):
    string =string.replace(":)", "🙂")
    string = string.replace(":(", "🙁")
    return string

def main():
    u_input = input("Enter a string: ")
    print(convert(u_input))

main()

