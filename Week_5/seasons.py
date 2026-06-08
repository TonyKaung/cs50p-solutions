from datetime import date
import sys
import inflect

p = inflect.engine()

def main():
    dob = input("Date of birth: ")
    # check format, exit if invalid
    try:
        dateOfBirth = date.fromisoformat(dob)
    except ValueError:
        sys.exit("Invalid date")

    minutes = minutes_since(dateOfBirth)
    print(f"{minutes_to_words(minutes)} minutes")

# returns the number of minutes since the given date
# assumes start and end is at midnight
def minutes_since(dateOfBirth, today=date.today()):
    days = today - dateOfBirth
    return days.days * 24 * 60

# change the number of minutes to words
def minutes_to_words(minutes):
    minutesInWords = p.number_to_words(minutes, andword="")
    return minutesInWords.capitalize()

if __name__ == "__main__":
    main()