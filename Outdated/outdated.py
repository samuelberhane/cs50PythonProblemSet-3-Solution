months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        date = input('Date: ')
        if "/" in date:
            date = date.strip()
            month,day,year = date.split("/")
        month = int(month)
        if (1 < month <= 12) and (1 < int(day) <= 31):
                break
    except:
        try:
            if "," in date:
                month,day,year = date.split(" ")
            for i in range(len(months)):
                if months[i] == month:
                    month = i + 1
            day = day.replace(",","")
            if (1 < int(month) <= 12) and (1 < int(day) <= 31):
                break
        except:
            pass
if (1 < int(month) < 10 and 1 < int(day) < 10):
    print(f"{year}-0{month}-0{day}")
elif (1 < int(month) < 10):
    print(f"{year}-0{month}-{day}")
elif (1 < int(day) < 10):
    print(f"{year}-{month}-0{day}")
else:
    print(f"{year}-{month}-{day}")