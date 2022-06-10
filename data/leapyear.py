from calendar import monthrange

def isleapyear(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

print(isleapyear(1900))


def howmanydaysinmonth(month, year):
    return monthrange(year, month)[1]

print(howmanydaysinmonth(2, 1996))


def howmanydays(month,year):
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    elif month == 2:
        if isleapyear(year):
            return 29
        else:
            return 30

print(howmanydays(2, 1996))