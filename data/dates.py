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

# 1. Predefined date
#date = "1-2-2016"

# 2. Date provided by user
date = input("Please input date")

# 3. Date read from file
# file = open('plik.txt')
# date = file.read()
# file.close()

datelist = re.split('[./\-: ]+', date, 3)

def dates(datelist):

    if len(datelist) == 1:
        year = int(datelist[0])
        return isleapyear(year)

    elif len(datelist) == 2:
        month = int(datelist[0])
        year = int(datelist[1])
        return howmanydays(month, year)

    elif len(datelist) == 3:
        day = int(datelist[0])
        month = int(datelist[1])
        year = int(datelist[2])
        return whatdayofmonth(day, month, year)


print(dates(datelist))
print(type(dates(datelist)))