import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # check if the string is a valid HTML tag
    # need to check the whole input so no ^ and $ in the regex
    match = re.search(r'src="https?://(?:www\.)?youtube\.com/embed/([\w-]+)"', s)
    if match:
        return f"https://youtu.be/" + match.group(1)
    else:
        return None

if __name__ == "__main__":
    main()