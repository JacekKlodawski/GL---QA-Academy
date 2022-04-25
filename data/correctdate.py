import re
from calendar import monthrange

def isleapyear(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False


def howmanydaysinmonth(month, year):
    return monthrange(year, month)[1]


def whatdayofyear(day, month, year):
    leap_year = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
    standard_year = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    if month in [1, 3, 5, 7, 8, 10, 12] and day in range(1, 32):
        return standard_year[month - 1] + day
    elif month in [4, 6, 9, 11] and day in range(1, 31):
        return standard_year[month - 1] + day
    elif month == 2:
        if isleapyear(year) and day in range(1, 30):
            return leap_year[month - 1] + day
        elif not isleapyear(year) and day in range(1, 29):
            return standard_year[month - 1] + day
        else:
            return ("No such day or month")
    else:
        return ("No such day or month")


def howmanydays(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if isleapyear(year):
            return 29
        else:
            return 28
    else:
        return ("There is no such month")

    # 1. Predefined date
date = "31a13a2000"

    #2. Date provided by user
#date = input("Please input date")

    # 3. Date read from file
# file = open('plik.txt')
# date = file.read()
# file.close()

datelist = re.split(r"\D", date)

def dates(datelist):

    year = int(datelist[-1])

    if len(datelist) == 1:
        return isleapyear(year)

    elif len(datelist) == 2:
        month = int(datelist[-2])
        return howmanydays(month, year)

    elif len(datelist) == 3:
        month = int(datelist[-2])
        day = int(datelist[-3])
        return whatdayofyear(day, month, year)

    else:
        return ("Something went wrong")

print(dates(datelist))