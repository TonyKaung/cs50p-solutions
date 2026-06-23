import random
import string
import re


def main():
    urls = {}  # short_code -> long_url mapping

    while True:
        choice = input("Shorten or Expand? (s/e/q to quit): ").strip().lower()

        if choice == "s":
            long_url = input("Enter URL to shorten: ").strip()
            # validate the URL using is_valid_url
            # if valid, generate a short code and store it in urls
            # print the short code to the user
            # if invalid, print an error message
            if is_valid_url(long_url):
                short_url = shorten_url(long_url, urls)
                print(short_url)
            else:
                print("Invalid URL")


        elif choice == "e":
            short_code = input("Enter short code to expand: ").strip()
            # use expand_url to look up the original URL
            # print it, or print an error if not found
            expanded_url = expand_url(short_code, urls)
            if expanded_url is not None:
                print(expanded_url)
            else:
                print("Code does not exist.")

        elif choice == "q":
            break

        else:
            print("Invalid option")


def is_valid_url(url):
    """Return True if url looks like a valid http/https URL, else False."""
    # use a regex to check the format
    pattern = r"^https?://[^\s]+$"
    return bool(re.match(pattern, url))


def generate_short_code(length=6):
    """Generate a random alphanumeric code of given length."""
    # use random.choices() with string.ascii_letters + string.digits
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))


def shorten_url(long_url, urls):
    """Generate a unique short code for long_url, store it in urls, and return the code."""
    # keep generating codes until you get one not already in urls
    # store it: urls[code] = long_url
    # return the code
    code = generate_short_code()
    while code in urls:
        code = generate_short_code()
    urls[code] = long_url
    return code


def expand_url(short_code, urls):
    """Return the original URL for a given short_code, or None if not found."""
    # look up short_code in urls and return the result (or None)
    return urls.get(short_code)


if __name__ == "__main__":
    main()