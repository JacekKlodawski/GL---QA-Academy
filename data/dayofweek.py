from calendar import monthrange

def whatdayofmonth(day, month, year):
    daysoftheweek = ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela']
    firstday = monthrange(year, month)[0]
    dayofweek = firstday - 1 + day % 7
    return daysoftheweek[dayofweek]

print(whatdayofmonth(1, 4, 2022))


