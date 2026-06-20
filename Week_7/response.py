import validators

def main():
    print(validate(input("What's your email? ")))

def validate(s):
    # validate email
    if validators.email(s):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()