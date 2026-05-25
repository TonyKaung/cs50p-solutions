while True:
    dates = input("Date: ").lower().strip()
    if "/" in dates:
        try:
            month, day, year = dates.split("/")
            month = int(month)
            day = int(day) 
            year = int(year)
            if not (1<= month <= 12 and 1 <= day <= 31 and year >= 0):
                continue
            print(f"{year:04d}-{month:02d}-{day:02d}")
            break
        except ValueError:
            continue
    else:
        try:
            month_day, year = dates.split(", ")
            month, day = month_day.split(" ")
            month = month.strip(",").lower()
            day = int(day)
            year = int(year)
            months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
            if month not in months or not (1 <= day <= 31 and year >= 0):
                continue
            month = months.index(month) + 1
            print(f"{year:04d}-{month:02d}-{day:02d}")
            break
        except ValueError:
            continue