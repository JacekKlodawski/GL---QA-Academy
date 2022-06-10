import re
from calendar import monthrange


def isleapyear(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False


def howmanydaysinmonth(month, year):
    return monthrange(year, month)[1]


def whatdayofmonth(day, month, year):
    daysoftheweek = ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela']
    firstday = monthrange(year, month)[0]
    dayofweek = (firstday + day) % 7 - 1
    return daysoftheweek[dayofweek]

# print("1. Use the default date")
# print("2. I want to input the date manually")
# print("3. I want to read the date from file")
# choice = input("How do you want to provide the date? Pick between 1-3.")

# datelist = re.split('[./\-: ]+', date)

def dates():

# 1. Predefined date
    #date = "2016"

# 2. Date provided by user
    date = input("Please input date")

# 3. Date read from file
    # file = open('plik.txt')
    # date = file.read()
    # file.close()

    datelist = re.split('[./\-: ]+', date, 3)

    if len(datelist) == 1:
        year = int(datelist[0])
        return isleapyear(year)

    elif len(datelist) == 2:
        month = int(datelist[0])
        year = int(datelist[1])
        return howmanydaysinmonth(month, year)

    elif len(datelist) == 3:
        day = int(datelist[0])
        month = int(datelist[1])
        year = int(datelist[2])
        return whatdayofmonth(day, month, year)

    else:
        print('Something went wrong')

print(dates())
print(type(dates()))