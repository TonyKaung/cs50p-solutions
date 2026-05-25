months = ["january", "february", "march", "april", "may", "june",
          "july", "august", "september", "october", "november", "december"]

while True:
    dates = input("Date: ").strip().lower()
    try:
        if "/" in dates:
            month, day, year = dates.split("/")
            month, day, year = int(month), int(day), int(year)
        else:
            month_day, year = dates.split(", ")
            month, day = month_day.split(" ")
            day, year = int(day), int(year)
            if month not in months:
                continue
            month = months.index(month) + 1
        if 1 <= month <= 12 and 1 <= day <= 31 and year >= 0:
            print(f"{year:04d}-{month:02d}-{day:02d}")
            break
    except ValueError:
        continue