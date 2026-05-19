def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    return f"{hours}:{minutes/60:.2f}"


def main():
    time = input("What time is it? ")
    converted_time = convert(time)
    if(converted_time >= "7:00" and converted_time <= "8:00"):
        print("breakfast time")
    elif(converted_time >= "12:00" and converted_time <= "13:00"):
        print("lunch time")
    elif(converted_time >= "18:00" and converted_time <= "19:00"):
        print("dinner time")
    elif("0:00" > converted_time or converted_time > "23:59"):
        print("Invalid time")

if __name__ == "__main__":
    main()