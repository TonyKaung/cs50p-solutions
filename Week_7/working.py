import re

def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        print("Invalid Input")

def convert(s):
    # check the format
    match = re.search(r"^([0-9][0-2]?):([0-5][0-9]) (AM|PM) to ([0-9][0-2]?):([0-5][0-9]) (AM|PM)$", s)
    # group hours, minutes, and AM or PM and turn hours and minutes into integers
    if match:
        start_hour = int(match.group(1))
        start_minute = match.group(2)
        start_period = match.group(3)
        end_hour = int(match.group(4))
        end_minute = match.group(5)
        end_period = match.group(6)

        # convert to 24-hour format
        if start_period == "PM" and start_hour != 12:
            start_hour += 12
        elif start_period == "AM" and start_hour == 12:
            start_hour = 0
        if end_period == "PM" and end_hour != 12:
            end_hour += 12
        elif end_period == "AM" and end_hour == 12:
            end_hour = 0
        
        return f"{start_hour:02d}:{start_minute} to {end_hour:02d}:{end_minute}"
    else:
        raise ValueError("Invalid Input")
    
    

if __name__ == "__main__":
    main()