day_strings = {
    0: 'Mon',
    1: 'Tue',
    2: 'Wed',
    3: 'Thur',
    4: 'Fri',
    5: 'Sat',
    6: 'Sun'
}

def is_leap(year):
    if year % 4:
        return False
    if year % 100:
        return True
    if year % 400 == 0:
        return True
    return False

def days_in_year(year):
    if is_leap(year):
        return 366
    return 365

def days_in_month(year, month):
    if month in [4, 6, 9, 11]:
        return 30
    if month == 2:
        return 29 if is_leap(year) else 28
    return 31

def day_of_year(year, month, day):
    days = day
    # Add previous months
    for m in range(1, month):
        days += days_in_month(year, m)
    return days

def day_since_epoch(year, month, day):
    days = 0
    for y in range(1900, year):
        days += days_in_year(y)
    return days + day_of_year(year, month, day) - 1

sundays = 0
for year in range(1901, 2001):
    for month in range(1, 13):
        days_since_epoch = day_since_epoch(year, month, 1)
        if days_since_epoch % 7 == 6:
            sundays += 1

print sundays
    
